import time

def Quick(A, first, last) :
    global nQuickcompare
    global nQuickswap

    if first == 0 and last == len(A) - 1 :
        start = time.clock()

    p = A[(first + last) / 2]
    left = first
    right = last

    while left <= right :
        nQuickcompare = nQuickcompare + 1
        while A[left] < p :
            nQuickcompare = nQuickcompare + 1
            left = left + 1
        while A[right] > p :
            nQuickcompare = nQuickcompare + 1
            right = right - 1
        if left <= right :
            nQuickcompare = nQuickcompare + 1
            nQuickswap = nQuickswap + 1
            A[left], A[right] = A[right], A[left]
            left = left + 1
            right = right - 1
    nQuickcompare = nQuickcompare + 1
    if first < right :
        Quick(A, first, right)
    nQuickcompare = nQuickcompare + 1
    if left < last :
        Quick(A, left, last)
    if first == 0 and last == len(A) - 1 :
        end = time.clock()
        return (nQuickcompare, nQuickswap , end - start)

in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)

global nQuickcompare
global nQuickswap
nQuickcompare = 0
nQuickswap = 0

a,b,c = Quick(B,0,len(B)-1)

print "Compare = %d Swap = %d time = %f" %(a,b,c)
