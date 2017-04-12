"""Sorting Algorithms

    This file includes all sorting algorithms existing in
    this project. It provides an interface to use them
    easily to sort lists and dictionaries.

    @author Florian Dahlitz
"""
def swap(collection, a, b):
    """swap

        Swaps two values of a given collection. Needs a pointer
        to the collection and the two positions of the
        values to swap.
    """
    tmp = collection[a]
    collection[a] = collection[b]
    collection[b] = tmp


class SortingAlgorithms:
    pass
