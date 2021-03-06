"""
Copyright 2017 Nikolay Stanchev

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


# Simple unittests for the ADT Stack
import unittest

from DataStructures.AbstractDataStructures import Stack
from DataStructures.Errors import *


class StackTest(unittest.TestCase):

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size, 0, "Stack size should be 0 at initialization")
        for i in range(1, 41):
            stack.push(i)
            stack.push(i+1)
            stack.pop()
        self.assertEqual(stack.size, 40, "Incorrect stack size")

        stack = Stack(str)
        self.assertEqual(stack.size, 0, "Stack size should be 0 at initialization")
        for l in ["a", "d", "b", "m"]:
            stack.push(l)

        stack.pop()
        self.assertEqual(stack.size, 3, "Incorrect stack size")

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.size == 0, "Stack should be empty")
        stack.push("word")
        stack.push("sentence")
        stack.pop()
        self.assertFalse(stack.size == 0, "Stack should not be empty")

        stack = Stack(int)
        self.assertTrue(stack.size == 0, "Stack should be empty")

        stack.push(0)
        self.assertFalse(stack.size == 0, "Stack should not be empty")

    def test_peek(self):
        stack = Stack()
        self.assertEqual(stack.peek(), None, "Top element of stack should be None at initialization")
        stack.push(2)
        stack.push("Tests")
        self.assertEqual(stack.peek(), "Tests", "Stack gives wrong peek")

        stack = Stack(float)
        self.assertEqual(stack.peek(), None, "Top element of stack should be None at initialization")
        stack.push(3.5)
        stack.push(1.27)
        stack.push(2.0)
        self.assertEqual(stack.peek(), 2.0, "Stack gives wrong peek")

    def test_pop(self):
        stack = Stack()
        with self.assertRaises(EmptyStackError):
            stack.pop()
        stack.push([1, 2, 3])
        self.assertEqual(stack.pop()[1], 2, "Stack pops wrong element")
        stack.push("pushed string")
        self.assertEqual(stack.pop(), "pushed string", "Stack pops wrong element")

        stack = Stack(bool)
        with self.assertRaises(EmptyStackError):
            stack.pop()
        stack.push(True)
        stack.push(False)
        stack.pop()
        self.assertTrue(stack.pop(), "Stack pops wrong element")

    def test_push(self):
        stack = Stack()
        stack.push(23)
        stack.push(20)
        self.assertEqual(stack.peek(), 20, "Wrong stack push implementation")
        self.assertEqual(len(stack), 2, "Wrong stack push implementation")

        stack = Stack(bool)
        with self.assertRaises(StackTypeError):
            stack.push("word")

        for i in range(10):
            if i % 2 == 0:
                stack.push(True)
            else:
                stack.push(False)
        self.assertEqual(stack.size, 10, "Wrong stack push implementation")

    def test_type(self):
        stack = Stack()
        self.assertEqual(stack.type, None)

        with self.assertRaises(StackTypeError):
            Stack(elements_type=3)

        stack = Stack(elements_type=list)
        self.assertEqual(stack.type, list)

        with self.assertRaises(StackTypeError):
            stack.push("hey")

        stack = Stack(elements_type=str)
        stack.push("world")
        stack.push("hello")
        test_string = stack.pop() + " " + stack.pop()
        self.assertEqual(test_string, "hello world", "Stack with strings doesn't pop correctly")

        with self.assertRaises(StackTypeError):
            stack.push(123)

    def test_str(self):
        stack = Stack(int)
        self.assertEqual(str(stack), "deque([])", "String representation of stack doesn't work with empty stacks")

        stack.push(0)
        self.assertEqual(str(stack), "deque([0])", "String representation of stack doesn't work with singleton stacks")

        for i in [5, 20, 11, 34, 2]:
            stack.push(i)

        self.assertEqual(str(stack), "deque([0, 5, 20, 11, 34, 2])",
                         "String representation of stack doesn't work with many elements")

        stack.peek()
        stack.pop()
        stack.pop()
        self.assertEqual(str(stack), "deque([0, 5, 20, 11])",
                         "String representation of stack doesn't work after pop and peek operations")

        stack = Stack()
        stack.push(2.5)
        stack.push(0)
        self.assertEqual(str(stack), "deque([2.5, 0])")

    def test_iterator(self):
        stack = Stack(int)

        for i in range(20, 42, 2):
            stack.push(i)

        integers = list(range(20, 42, 2))
        self.assertEqual(len(stack), len(integers), "Size method doesn't work")

        index = len(integers) - 1
        for num in stack:
            self.assertEqual(num, integers[index], "Iterator doesn't work")
            index -= 1

        self.assertEqual(len(stack), 0, "iterator doesn't adjust stack size")

    def test_contains(self):
        stack = Stack()
        self.assertFalse(1 in stack, "Stack contains method doesn't work")

        stack.push("word")
        self.assertEqual("word" in stack, stack.contains("word"), "Stack contains method doesn't work")
        self.assertTrue(stack.contains("word"), "Stack contains method doesn't work")

        stack = Stack(elements_type=float)
        stack.push(1.55)
        stack.push(2.3)
        self.assertTrue(2.3 in stack, "Stack contains method doesn't work")
        self.assertTrue(stack.contains(1.55), "Stack contains method doesn't work")

        with self.assertRaises(StackTypeError):
            _ = 4 in stack

        with self.assertRaises(StackTypeError):
            stack.contains("word")

    def test_remove(self):
        stack = Stack()
        with self.assertRaises(StackElementError):
            stack.remove(5)

        stack.push(5)
        stack.push("str")
        stack.push(5.5)
        self.assertEqual(stack.peek(), 5.5)
        self.assertEqual(len(stack), 3)
        stack.remove(5.5)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), "str", "Wrong remove implementation")

        stack = Stack(int)
        with self.assertRaises(StackTypeError):
            stack.remove("string")
        for i in range(10):
            stack.push(i)
        stack.remove(0)
        stack.remove(1)
        self.assertEqual(str(stack), "deque(" + str(list(range(2, 10))) + ")", "Wrong remove implementation")
        stack.remove(5)
        stack.remove(9)
        self.assertEqual(str(stack), "deque([2, 3, 4, 6, 7, 8])", "Wrong remove implementation")
        self.assertEqual(stack.pop(), 8, "Wrong remove implementation")


if __name__ == '__main__':
    unittest.main()
