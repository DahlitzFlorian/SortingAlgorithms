"""Sorting Algorithms

    This file includes all sorting algorithms existing in
    this project. It provides an interface to use them
    easily to sort lists.

    @author Florian Dahlitz
"""
def swap(list, a, b):
    """swap

        Swaps two values of a given lists. Needs a pointer
        to the lists and the two positions of the
        values to swap.
    """
    tmp = list[a]
    list[a] = list[b]
    list[b] = tmp


def bubble_sort(data):
    """Bubble Sort

        This algorithm sorts by comparing neighboring values.
        Average: O(n^2)
    """
    for j in range(0, len(data)):
        for i in range(0, len(data) - 1):
            if data[i] > data[i+1]:
                swap(data, i, i+1)
    
    return data


class SortingAlgorithms:
    bubble_sort = staticmethod(bubble_sort)
