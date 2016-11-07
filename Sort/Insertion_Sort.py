import time

def Insertion(A):
    start = time.clock()
    nInsert_compare = 0
    nInsert_swap = 0
    for i in range(1,len(A)):
        j = i
        for j in range(i,0, -1):
            nInsert_compare = nInsert_compare + 1
            if A[j] < A[j-1]:
                nInsert_swap = nInsert_swap + 1
                A[j], A[j-1] = A[j-1], A[j]
    end = time.clock()
    print A
    return nInsert_compare, nInsert_swap, end-start

in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)

print B

a, b, c = Insertion(B)


print "Compare = %d Swap= %d  time= %f" % (a,b,c)
