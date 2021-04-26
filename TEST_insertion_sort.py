import unittest
import insertion_sort as isort

class TestGetData(unittest.TestCase):

    def test_get_data_index_equal(self):
        array = [6, 5, 4, 34, 8, 9]
        self.assertEqual(isort.get_data(array, 0), 6)
        self.assertEqual(isort.get_data(array, 1), 5)
        self.assertEqual(isort.get_data(array, 2), 4)
        self.assertEqual(isort.get_data(array, 3), 34)
        self.assertEqual(isort.get_data(array, 4), 8)
        self.assertEqual(isort.get_data(array, 5), 9)

    def test_get_data_index_not_equal(self):
        array = [6, 5, 4, 34, 8, 9]
        self.assertNotEqual(isort.get_data(array, 0), 5)
        self.assertNotEqual(isort.get_data(array, 1), 34)
        self.assertNotEqual(isort.get_data(array, 2), 8)
        self.assertNotEqual(isort.get_data(array, 3), 4)
        self.assertNotEqual(isort.get_data(array, 4), 9)
        self.assertNotEqual(isort.get_data(array, 5), 99)

class testSwap(unittest.TestCase):

    def test_swap_equal(self):
        array = [6, 5, 4, 34, 8, 9]
        self.assertEqual(isort.swap(array, 1, 0), [5, 6, 4, 34, 8, 9])
        self.assertEqual(isort.swap(array, 5, 0), [9, 5, 6, 4, 34, 8])
        self.assertEqual(isort.swap(array, 4, 3), [9, 5, 6, 34, 4, 8])

    def test_swap_not_equal(self):
        array = [6, 5, 4, 34, 8, 9]
        self.assertNotEqual(isort.swap(array, 1, 0),[6, 5, 4, 34, 8, 9])

if __name__ == '__main__':
    unittest.main()