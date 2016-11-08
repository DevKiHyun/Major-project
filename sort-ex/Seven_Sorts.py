import time
import math

def Bubble(A):
    start = time.clock()
    nBubble_compare = 0
    nBubble_swap = 0
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            nBubble_compare = nBubble_compare + 1
            if A[j-1] > A[j] :
                nBubble_swap = nBubble_swap + 1
                A[j-1], A[j] = A[j], A[j-1]
    end = time.clock()
    return (nBubble_compare, nBubble_swap, end-start , A)

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
    return (nHeapcompare, nHeapswap, end - start, A)

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
    return (nSelect_compare, nSelect_swap, end-start, A)

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
    return (nInsert_compare, nInsert_swap, end-start, A)

def Merge_sort(A,first,last):

    global nMergecompare
    global nMergeswap
    nMergecompare += 1
    if first < last :
        mid = (first + last)/2
        Merge_sort(A,first,mid)
        Merge_sort(A,mid+1,last)
        Merge(A,first,last)
    return nMergecompare, nMergeswap , A

def Merge(A,first,last) :
    global nMergecompare
    global nMergeswap
    temp = []
    mid = (first+last)/2
    i , j , k = first, mid +1, 0
    while i <= mid and j <= last :
        nMergecompare += 3
        if A[i] <= A[j] :
            temp.append(A[i])
            k = k + 1
            i = i + 1
        else :
            temp.append(A[j])
            k = k + 1
            j = j + 1
    for i in range(i,mid+1,1) :
        temp.append(A[i])
        k = k + 1
    for j in range(j,last,1) :
        temp.append(A[j])
        k = k + 1
    b = first
    for a in range(0,k) :
        A[b] = temp[a]
        b = b + 1

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
        return (nQuickcompare, nQuickswap , end - start, A)

def Radix(A):
    start = time.clock()
    cnt = int(math.log10(max(A)))
    nRadixcompare = 0
    nRadixswap = 0
    n = len(A)
    i = 1
    for k in range(cnt+1) :
        zero, one, two, three, four, five, six, seven, eight, nine = [], [], [], [], [], [], [], [], [], []
        for j in range(n):
            nRadixcompare = nRadixcompare + 3
            if i == 1 :
                nRadixcompare = nRadixcompare + 10
                if A[j] % 10 == 0 :
                    zero.append(A[j])
                elif A[j] % 10 == 1 :
                    one.append(A[j])
                elif A[j] % 10 == 2 :
                    two.append(A[j])
                elif A[j] % 10 == 3 :
                    three.append(A[j])
                elif A[j] % 10 == 4 :
                    four.append(A[j])
                elif A[j] % 10 == 5 :
                    five.append(A[j])
                elif A[j] % 10 == 6 :
                    six.append(A[j])
                elif A[j] % 10 == 7 :
                    seven.append(A[j])
                elif A[j] % 10 == 8 :
                    eight.append(A[j])
                elif A[j] % 10 == 9 :
                    nine.append(A[j])

            else :
                k = pow(10, i-1)
                nRadixcompare = nRadixcompare + 10
                N = A[j]%pow(10, i)

                if N / k == 0 :
                    zero.append(A[j])
                if N / k == 1 :
                    one.append(A[j])
                if N / k == 2 :
                    two.append(A[j])
                if N / k == 3 :
                    three.append(A[j])
                if N / k == 4 :
                    four.append(A[j])
                if N / k == 5 :
                    five.append(A[j])
                if N / k == 6 :
                    six.append(A[j])
                if N / k == 7 :
                    seven.append(A[j])
                if N / k == 8 :
                    eight.append(A[j])
                if N / k == 9 :
                    nine.append(A[j])
        A = zero + one + two + three + four + five + six + seven + eight + nine
        i = i + 1
    end = time.clock()
    return (nRadixcompare, nRadixswap, end - start, A)

def check_sort(A):
    n = len(A)
    for i in range(1,n):
        if A[i-1] > A[i] : return False
    return True

in_file = open('sort.txt', 'r')
array = list(in_file.read().split())
in_file = open('analyze_sort.txt', 'a')
n = len(array)
in_file.write(str(n)+ ' ')
A = map(int, array)
B = map(int, array)
C = map(int, array)
D = map(int, array)
E = map(int, array)
F = map(int, array)
G = map(int, array)

a,b,c, arr = Bubble(A)
print "Bubble : Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
in_file.write(str(c)+ ' ')

a,b,c, arr = Heap(A)
print "Heap : Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
in_file.write(str(c)+ ' ')

a,b,c, arr = Selection(A)
print "Selection : Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
in_file.write(str(c)+ ' ')

a,b,c, arr = Insertion(A)
print "Insertion : Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
in_file.write(str(c)+ ' ')

global nMergecompare
global nMergeswap
nMergecompare = 0
nMergeswap = 0

start = time.clock()
a,b,arr = Merge_sort(A,0,len(A)-1)
end = time.clock()
c = end - start
print "Merge : Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
in_file.write(str(c)+ ' ')

global nQuickcompare
global nQuickswap
nQuickcompare = 0
nQuickswap = 0

a,b,c, arr = Quick(A,0,len(A)-1)
print "Quick : Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
in_file.write(str(c)+ ' ')

a,b,c, arr = Radix(A)
print "Radix : Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
in_file.write(str(c)+ ' ' + '\n')
