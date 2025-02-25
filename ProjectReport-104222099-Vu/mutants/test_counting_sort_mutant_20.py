import unittest
from counting_sort_mutant_20 import counting_sort

class TestCountingSort(unittest.TestCase):
    
    def test_basic_functionality(self):
        self.assertEqual(counting_sort([4, 2, 5, 2, 3]), [2, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_negative_numbers(self):
        self.assertEqual(counting_sort([-2, -5, -45]), [-45, -5, -2])

    def test_all_same_numbers(self):
        self.assertEqual(counting_sort([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_element_duplication(self):
        original = [1, 2, 3]
        duplicated = original * 2  # Duplicate elements
        self.assertEqual(counting_sort(duplicated), [1, 1, 2, 2, 3, 3])

    def test_scale_elements(self):
        original = [3, 1, 4, 1, 5]
        scaled = [x * 2 for x in original]
        expected = [x * 2 for x in counting_sort(original)]
        self.assertEqual(counting_sort(scaled), expected)

    def test_concatenation_sorted_arrays(self):
        sorted_a = [1, 2, 3]
        sorted_b = [4, 5, 6]
        concatenated_and_sorted = counting_sort(sorted_a + sorted_b)
        self.assertEqual(concatenated_and_sorted, sorted_a + sorted_b)
        

if __name__ == "__main__":
    unittest.main()
