import unittest

from sort.SortingAlgorithms import SortingAlgorithms


class TestAlgorithms(unittest.TestCase):
    """
    This class includes test to check the correct working of the 
    algorithms included in this package.
    """
    def test_bubble_sort(self):
        """
        Checks the bubble-sort-algorithm.
        """

        # creating sample lists
        list1 = [3,]
        list2 = [23, 34]
        list3 = [154, 10, 6742, 7, 29, 364]

        # sort the lists
        SortingAlgorithms.bubble_sort(list1)
        SortingAlgorithms.bubble_sort(list2)
        SortingAlgorithms.bubble_sort(list3)

        # check the lists
        self.assertEqual(list1, [3,])
        self.assertEqual(list2, [23, 34])
        self.assertEqual(list3, [7, 10, 29, 154, 364, 6742])
    
    def test_riplle_sort(self):
        """
        Checks the ripple-sort-algorithm.
        """

        # creating sample lists
        list1 = [3,]
        list2 = [23, 34]
        list3 = [154, 10, 6742, 7, 29, 364]

        # sort the lists
        SortingAlgorithms.ripple_sort(list1)
        SortingAlgorithms.ripple_sort(list2)
        SortingAlgorithms.ripple_sort(list3)

        # check the lists
        self.assertEqual(list1, [3,])
        self.assertEqual(list2, [23, 34])
        self.assertEqual(list3, [7, 10, 29, 154, 364, 6742])

    def test_min_sort(self):
        """
        Checks the min-sort-algorithm.
        """

        # creating sample lists
        list1 = [3,]
        list2 = [23, 34]
        list3 = [154, 10, 6742, 7, 29, 364]

        # sort the lists
        SortingAlgorithms.min_sort(list1)
        SortingAlgorithms.min_sort(list2)
        SortingAlgorithms.min_sort(list3)

        # check the lists
        self.assertEqual(list1, [3,])
        self.assertEqual(list2, [23, 34])
        self.assertEqual(list3, [7, 10, 29, 154, 364, 6742])

    def test_quick_sort(self):
        """
        Checks the quick-sort-algorithm.
        """

        # creating sample lists
        list1 = [3,]
        list2 = [23, 34]
        list3 = [154, 10, 6742, 7, 29, 364]

        # sort the lists
        SortingAlgorithms.quick_sort(list1, 0, len(list1) - 1)
        SortingAlgorithms.quick_sort(list2, 0, len(list2) - 1)
        SortingAlgorithms.quick_sort(list3, 0, len(list3) - 1)

        # check the lists
        self.assertEqual(list1, [3,])
        self.assertEqual(list2, [23, 34])
        self.assertEqual(list3, [7, 10, 29, 154, 364, 6742])


if __name__ == "__main__":
    unittest.main()
