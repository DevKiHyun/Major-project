import time


def heapify(A,n,k):
    while 2*k+1 < n:
        global nHeapcompare
        global nHeapswap
        nHeapcompare = nHeapcompare + 1
        L = 2*k+1
        R = 2*k+2
        nHeapcompare = nHeapcompare + 5
        if A[k] < A[L] : m = L
        else : m = k
        if R < n and A[R] > A[m] : m = R
        if k != m :
            nHeapswap = nHeapswap + 1
            A[k] , A[m] = A[m], A[k]
            k = m
        else : break

def make_heap(A):
    n = len(A)
    for k in range(n/2,-1,-1) :
        heapify(A,n,k)

def Heap(A):
    global nHeapcompare
    global nHeapswap
    nHeapcompare = 0
    nHeapswap = 0
    start = time.clock()
    make_heap(A)
    n = len(A)
    for k in range(len(A)-1) :
        nHeapswap = nHeapswap + 1
        A[0] , A[n-1] = A[n-1], A[0]
        n = n-1
        heapify(A,n,0)
    end = time.clock()
    return (nHeapcompare, nHeapswap, end - start)





in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)

a , b, c = Heap(B)

print B

print "Compare = %d Swap= %d  time= %f" % (a,b,c)
