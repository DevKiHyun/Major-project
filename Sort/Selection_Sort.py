import time

def Selection(A) :
    start = time.clock()
    nSelect_compare = 0
    nSelect_swap = 0
    for i in range(0, len(A)):
        m = i
        for j in range(i, len(A)):
            nSelect_compare = nSelect_compare + 1
            if A[j]  < A[m]:
                m = j
        nSelect_swap = nSelect_swap + 1
        A[m],A[i] = A[i], A[m]
    end = time.clock()
    print A
    return nSelect_compare, nSelect_swap, end-start

in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)

(a,b,c) = Selection(B)
print "Compare = %d Swap= %d time= %f" % (a,b,c)
