import time

def Merge_sort(A,first,last):

    global nMergecompare
    global nMergeswap
    nMergecompare += 1
    if first < last :
        mid = (first + last)/2
        Merge_sort(A,first,mid)
        Merge_sort(A,mid+1,last)
        Merge(A,first,last)
    return nMergecompare, nMergeswap


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
        nMergecompare = nMergecompare + 1
        temp.append(A[i])
        k = k + 1
    for j in range(j,last,1) :
        nMergecompare = nMergecompare + 1
        temp.append(A[j])
        k = k + 1
    b = first
    for a in range(0,k) :
        nMergecompare = nMergecompare + 1
        A[b] = temp[a]
        b = b + 1

in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)
global nMergecompare
global nMergeswap
nMergecompare = 0
nMergeswap = 0

#start = time.clock()
a , b= Merge_sort(B,0,len(B)-1)
#end = time.clock()
#c = end - start

print B

print "Compare = %d Swap= %d  time= %f" % (a,b,c)
