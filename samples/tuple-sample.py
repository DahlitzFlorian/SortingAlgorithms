from sort.SortTuples import SortTuples
import random


# first provide a tuple of numbers (here integers)
list1 = []
for i in range(1000):
    list1.append(random.randint(0,1000))

# given tuple which should be sorted
tuple1 = tuple(list1)

# print unsorted tuple
print("########## Unsorted tuple ##########")
print(tuple1)

# sort the tuple
tuple1 = SortTuples.sort_tuple(tuple1)

# print sorted tuple
print("########## Sorted tuple ##########")
print(tuple1)
