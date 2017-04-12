"""Sort Tuples

    Makes use of SortingAlgorithms and sorts tuples with
    the Quick-Sort-algorithm.

    @author Florian Dahlitz
"""
from sort.SortingAlgorithms import SortingAlgorithms


def sort_tuple(data: tuple) -> tuple:
    """Sort Tuple

        Sorts a given tuple not containing tuples, lists and
        dictionaries.
    """
    data_list = list(data)

    return tuple(SortingAlgorithms.quick_sort(data_list, 0, len(data_list) - 1))


class SortTuples:
    """SortTuples-class
    
        Provides the sorting algorithms for tuples.
    """
    sort_tuple = staticmethod(sort_tuple)
