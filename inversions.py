# load saved list
import pandas as pd
test = pd.read_csv('inversions_test', names=['Numbers'])
test = test.values.tolist()
print len(test)

# count inversions recursively
def count_inv(X):
    if len(X)<=1:
        # return tuple with (number of inversions, sorted array)
        return (0,X)
    # break X in two and make recursive calls
    # Sort and count inversions for each half
    n = len(X)
    if n%2==0:
        a = count_inv(X[:(n/2)])
        count_a = a[0]
        A = a[1]
        b = count_inv(X[n/2:])
        count_b = b[0]
        B = b[1]

    else:
        a = count_inv(X[:n/2])
        count_a = a[0]
        A = a[1]
        b = count_inv(X[n/2:])
        count_b = b[0]
        B = b[1]

    # Sort arrays returned and count split inversions
    # instantiate pointers for a and b
    i = 0
    j = 0
    count = 0
    C = []   # if I really wanted to optimize efficiency, this would be a numpy array.
    while i<len(A) and j<len(B):
        if B[j] < A[i]:
            C.append(B[j])
            count = count + len(A) - i
            j += 1
        else:
            C.append(A[i])
            i +=1

    if i < len(A):
        # Every remaining element of A after is an inversion
        # count += len(A) -1 - i  #last index minus i
        C = C + A[i:]
    else:
        C = C + B[j:]
    # Count total inversions
    count = count + count_a + count_b

    # Return tuple with (number of inversions, sorted array)
    return (count, C)

print "total inversion count:"
print count_inv(test)[0]
