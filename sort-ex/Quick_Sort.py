import time

def Quick(A, first, last) :
    left = first + 1
    right = last
    if first >= last : return A
    #while left <= right :
    while left <= last and A[left] < A[first] :
            left = left +1
    while right > first and A[right] >= A[first] :
            right = right -1
    if left <= right:
            A[left] , A[right] = A[right] , A[left]
            left = left + 1
            right = right -1
    A[first], A[last] = A[last], A[first]
    Quick(A,first,right-1)
    Quick(A,right+1, last)
    return A


in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)
print B
print Quick(B,0,len(B)-1)
