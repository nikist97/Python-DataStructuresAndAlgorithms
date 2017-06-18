# Simple unittests for the merge_sort method
import unittest

from Algorithms.SortingAlgorithms import merge_sort


class MergeSortTest(unittest.TestCase):

    def test_empty(self):
        empty_list = []
        empty_list = merge_sort(empty_list)
        self.assertEqual(empty_list, [], "Merge sort gives wrong results with empty lists")
        new_list = merge_sort(empty_list)
        self.assertEqual(new_list, empty_list, "Merge sort gives wrong results with empty lists")

    def test_singleton(self):
        singleton = [5]
        singleton = merge_sort(singleton)
        self.assertEqual(singleton, [5], "Merge sort gives wrong results with singletons")

        singleton = ["string"]
        sorted_singleton = merge_sort(singleton)
        self.assertEqual(sorted_singleton, singleton, "Merge sort gives wrong results with singletons")

    def test_normal_list(self):
        # no repetitions in the list
        list_of_numbers = [5, 19, 2, -122, 120, 11, 356, -47, 81, 90, 122, 47, -122]
        list_of_numbers = merge_sort(list_of_numbers)
        self.assertEqual(list_of_numbers, [-122, -122, -47, 2, 5, 11, 19, 47, 81, 90, 120, 122, 356],
                         "Merge sort gives wrong results with a list with no repetitions")

        # repetitions in the list
        list_of_numbers = [5, 19, 2, 122, 120, 11, 356, 47, 81, 90, 2, 2, 5, 122, 123]
        new_list_of_numbers = merge_sort(list_of_numbers)
        self.assertEqual(new_list_of_numbers, [2, 2, 2, 5, 5, 11, 19, 47, 81, 90, 120, 122, 122, 123, 356],
                         "Merge sort gives wrong results with a list with no repetitions")

        # random list
        import random
        merge_sorted_list = []
        python_sorted_list = []
        for i in range(50):
            num = random.randint(1, 100)
            merge_sorted_list.append(num)
            python_sorted_list.append(num)
        python_sorted_list.sort()
        merge_sorted_list = merge_sort(merge_sorted_list)

        self.assertEqual(merge_sorted_list, python_sorted_list,
                         "Merge sort produces wrong results with random list")

        # testing strings with no repetitions
        strings_list = ["world", "hello", "python", "programming", "coding", "Tests"]
        strings_list = merge_sort(strings_list)
        python_sorted_strings = ["world", "hello", "python", "programming", "coding", "Tests"]
        python_sorted_strings.sort()

        self.assertEqual(strings_list, python_sorted_strings,
                         "Merge sort produces wrong results with strings with no repetitions")

        # testing strings with repetitions
        strings_list = ["world", "hello", "python", "programming", "code", "Tests", "world", "hello", "python", "hello"]
        strings_list = merge_sort(strings_list)
        python_sorted_strings = ["world", "hello", "python", "programming", "code", "Tests", "world", "hello", "python",
                                 "hello"]
        python_sorted_strings.sort()

        self.assertEqual(strings_list, python_sorted_strings,
                         "Merge sort produces wrong results with strings with repetitions")

if __name__ == '__main__':
    unittest.main()