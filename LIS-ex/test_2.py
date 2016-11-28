import time

def findSubsequence(A):
    start = time.clock()
    LIS = [0]*len(A)
    for i in range (len(A)):
        max = -1
        for j in range(i):
            if A[i] > A[j] :
                if max == -1 or max < LIS[j] + 1 :
                    max = 1 + LIS[j]
        if max == -1 :
            max = 1;
        LIS[i] = max;

    result = -1
    index = -1
    for i in range(len(LIS)) :
        if result < LIS[i] :
            result = LIS[i]
            index = i

    path = str(A[index]) + " "
    res = result -1
    for i in range(index-1,-1,-1) :
        if LIS[i] == res:
            path = str(A[i]) + " " + path
            res = res - 1



    print path

#in_file = open('LIS.txt', 'r')
#A = list(in_file.read().split())

A = [7, 6, 5, 4, 3, 2, 1, 8, 3, 1, 4, 2, 3, 4, 7, 5, 0, 2,3, 4, 7, 5]
A = map(int, A)


findSubsequence(A)
