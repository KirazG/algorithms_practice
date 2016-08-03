# This is not actually quicksort.
# This algorithm takes the first element of each array as pivot by default
# No randomization occurs
# Also counts the number of operations made for online grading.


# Come back and write a real quicksort later?

import numpy as np

X = np.genfromtxt('QuickSort_data.txt', delimiter='\n')


def quicksort(A, count=0):
    print A
    if len(A) <= 1:
        return (A, 0)

    # Pick pivot and move to front if not already there
    p = A[0]

    # Partition array
    i = 1
    j = 1

    while j < len(A):
        # partition
        if A[j] < p:
            swap = A[i]
            A[i] = A[j]
            A[j] = swap
            i += 1
        j += 1

    # swap pivot with ith element to put it in place
    # i may be > j if every single element in array gets swapped

    swap = A[i-1]
    A[i-1] = p
    A[0] = swap

    # Call quicksort on each subarray
    # return array that is concatenation of arrays, count that is sum of counts
    first = quicksort(A[:i-1])
    last = quicksort(A[i:])
    # first[0] is sorted array.  first[1] is count of comparisons in first half
    return (np.concatenate([first[0], [p], last[0]]), first[1]+last[1]+len(A)-1)

test = [3,8,2,5,1,4,7,6]

print quicksort(X)
