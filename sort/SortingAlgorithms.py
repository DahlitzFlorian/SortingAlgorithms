"""Sorting Algorithms

    This file includes all sorting algorithms existing in
    this project. It provides an interface to use them
    easily to sort lists.

    @author Florian Dahlitz
"""
def _swap(list, a, b):
    """swap

        Swaps two values of a given lists. Needs a pointer
        to the lists and the two positions of the
        values to swap.
    """
    tmp = list[a]
    list[a] = list[b]
    list[b] = tmp


def bubble_sort(data: list) -> list:
    """Bubble Sort

        This algorithm sorts by comparing neighboring values.
        Average: O(n^2)
    """
    for j in range(0, len(data)):
        for i in range(0, len(data) - 1):
            if data[i] > data[i+1]:
                _swap(data, i, i+1)
    
    return data


def ripple_sort(data: list) -> list:
    """Ripple Sort

        Does the same like Bubble-Sort but vice versa.
    """
    for j in range(0, len(data) - 1):  
        for i in range(j + 1, len(data)):
            if data[j] > data[i]:
                _swap(data, j, i)

    return data


def min_sort(data: list) -> list:
    """Min Sort

        Efficient algorithm, 'cause after every run it
        has to compare one less.
    """
    for j in range(0, len(data)):
        current_place = j
        value = current_place
        for i in range(j + 1, len(data)):
            if data[i] < data[value]:
                value = i
        _swap(data, value, current_place)
    
    return data


def quick_sort(data: list, left: int, right: int) -> list:
    """Quick Sort

        As the name mentions it's a very efficient and fast
        sorting algorithm.
    """
    l = left
    r = right
    comparison = data[int((l + r) / 2)]
    
    while l <= r:
        while data[l] < comparison:
            l += 1
        
        while data[r] > comparison:
            r -= 1
      
        if l <= r:
            _swap(data, l, r)
            l += 1
            r -= 1
    
    if left < r:
        quick_sort(data, left, r)
    
    if l < right:
        quick_sort(data, l, right)

    return data


class SortingAlgorithms:
    """SortingAlgorithms-Class

        Provides the sorting algorithms as static methods.
    """
    bubble_sort = staticmethod(bubble_sort)
    ripple_sort = staticmethod(ripple_sort)
    min_sort = staticmethod(min_sort)
    quick_sort = staticmethod(quick_sort)
