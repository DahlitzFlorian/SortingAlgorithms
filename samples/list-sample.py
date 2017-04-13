from sort.SortingAlgorithms import SortingAlgorithms
import random

# create lists of random integers
# need second list, because the sorting algorithms
# sort the list itself (and returns as well)
list1 = []
list2 = []
for i in range(10):
    list1.append(random.randint(0,1000))
    list2.append(random.randint(0,1000))

# print unsorted list1
print("########## Unsorted list1 ##########")
print(list1)

# sort the integers with bubble-sort
SortingAlgorithms.bubble_sort(list1)

# print bubble-sorted list
print("########## Bubble-sorted list ##########")
print(list1)

# print unsorted list2
print("########## Unsorted list2 ##########")
print(list2)

# sort with quick-sort
# the second argument (left) is the first index of the list
# the third argument (right) is the last index of the list
SortingAlgorithms.quick_sort(list2, 0, len(list2) - 1)

# print the quick-sorted list
print("########## Quick-sorted list ##########")
print(list2)
