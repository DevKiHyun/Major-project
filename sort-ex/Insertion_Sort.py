import time

def Insertion(A):
    start = time.clock()
    nInsert_compare = 0
    nInsert_swap = 0
    for i in range(1,len(A)):
        j = i - 1
        k = A[i]
        while A[j] > k and j >= 0:
            nInsert_compare = nInsert_compare + 1
            nInsert_swap = nInsert_swap + 1
            A[j+1] = A[j]
            j = j -1
        A[j+1] = k
    end = time.clock()

    return nInsert_compare, nInsert_swap, end-start , A


def check_sort(A):
    n = len(A)
    for i in range(1,n):
        if A[i-1] > A[i] : return False
    return True

in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)


a, b, c,arr = Insertion(B)


print "Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
