import unittest
import insertion_sort as isort


class TestInsertionSort(unittest.TestCase):
    
    def test_sort(self):
        array = [9, 19, 85, 99, 32, 0, 33, 123, 34, 33, 12, 0, -4, 16, 44, 2]
        self.assertEqual(isort.insertion_sort(array),
                [-4, 0, 0, 2, 9, 12, 16, 19, 32, 33, 33, 34, 44, 85, 99, 123])

class TestSwap(unittest.TestCase):

    def test_swap_equal(self):
        array = [6, 5, 4, 34, 8, 9]
        isort.swap(array, 1)
        self.assertEqual(array, [5, 6, 4, 34, 8, 9])
        isort.swap(array, 5)
        self.assertEqual(array, [5, 6, 4, 34, 9, 8])
        isort.swap(array, 4)
        self.assertEqual(array, [5, 6, 4, 9, 34, 8])

    def test_swap_not_equal(self):
        array = [6, 5, 4, 34, 8, 9]
        self.assertNotEqual(isort.swap(array, 1),[6, 5, 4, 34, 8, 9])

if __name__ == '__main__':
    unittest.main()