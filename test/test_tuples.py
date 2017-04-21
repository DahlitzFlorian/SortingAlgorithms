import unittest

from sort.SortTuples import SortTuples


class TestSortingTuples(unittest.TestCase):
    """
    This class includes tests to check the correct working
    of the sorting of tuples.
    """
    def test_sort_tuples(self):
        """
        sort_tuple
        """

        # create sample tuples
        tuple1 = (5,)
        tuple2 = (78, 154)
        tuple3 = (45, 9, 120, 63, 4579, 12, 3487)

        # sort the tuples
        tuple1 = SortTuples.sort_tuple(tuple1)
        tuple2 = SortTuples.sort_tuple(tuple2)
        tuple3 = SortTuples.sort_tuple(tuple3)

        # check the tuples
        self.assertEqual(tuple1, (5,))
        self.assertEqual(tuple2, (78, 154))
        self.assertEqual(tuple3, (9, 12, 45, 63, 120, 3487, 4579))


if __name__ == "__main__":
    unittest.main()
