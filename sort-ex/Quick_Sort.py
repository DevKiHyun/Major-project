import time

def Quick(A, first, last) :
    global nQuickcompare
    global nQuickswap
    if first == 0 and last == len(A)-1 :
        start = time.clock()
    left = first + 1
    right = last
    nQuickcompare = nQuickcompare + 1
    if first >= last : return A
    while left <= right :
        nQuickcompare = nQuickcompare + 1
        while left <= last and A[left] < A[first] :
            nQuickcompare = nQuickcompare + 1
            left = left +1
        while right >= first+1 and A[right] >= A[first] :
            nQuickcompare = nQuickcompare + 1
            right = right -1
        nQuickcompare = nQuickcompare + 1
        if left <= right:
            nQuickswap = nQuickswap + 1
            A[left] , A[right] = A[right] , A[left]
            left = left + 1
            right = right -1
    nQuickswap = nQuickswap + 1
    A[first], A[right] = A[right], A[first]
    Quick(A,first,right-1)
    Quick(A,right+1, last)
    if first == 0 and last == len(A)-1 :
        end = time.clock()
        return (nQuickcompare, nQuickswap, end - start)


in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)
print B

global nQuickcompare
global nQuickswap
nQuickcompare = 0
nQuickswap = 0

a,b,c = Quick(B,0,len(B)-1)

print "Compare = %d Swap = %d time = %f" %(a,b,c)
