import time

def findSubsequence(A):
    start = time.clock()
    check_cnt = 0

    LIS = [1]*1 + [0]*(len(A)-1)
    for i in range (len(A)):
        temp = 0
        for j in range(0,i):
            if A[i] > A[j] :
                if  temp < LIS[j] + 1:
                    temp = LIS[j] + 1
            elif A[i] == A[j] :
                temp = LIS[j]
        if temp == 0:
            temp = 1

        if i == 0 :
            LIS[i] = 1
        else :
            LIS[i] = temp;

    max_LIS = max(LIS)

    for i in range(len(LIS)) :
        if LIS[i] == max_LIS :
            max_loca = i


    output = ""
    temp_LIS = max_LIS - 1

    for k in range(max_loca - 1,-1,-1) :
            if LIS[k+1] == max_LIS :
                output = str(A[k+1]) + output
            if temp_LIS == LIS[k]:
                output = str(A[k]) + " " + output
                temp_LIS = temp_LIS - 1
    print max_LIS
    print output

in_file = open('LIS.txt', 'r')
A = list(in_file.read().split())

#A = [7, 6, 5, 4, 3, 2, 1, 8, 3, 1, 4, 2, 3, 4, 7, 5, 0, 2,3, 4, 7, 5]
A = map(int, A)

findSubsequence(A)
