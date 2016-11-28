import time

def LIS(A):
    start = time.clock()
    S = [1]*1 + [0]*(len(A)-1)
    for j in range(1,len(A)):
        temp = A[j]
        i = j-1
        if A[j] < A[j-1] :
            while temp < A[i] :
                if i == 0:
                    break
                i = i - 1
            if i == 0 :
                S[j] = S[i]
            else :
                S[j] = S[i] + 1
        elif A[j] > A[j-1] :
            S[j] = S[j-1] + 1
        elif A[j] == A[j-1] :
            S[j] == S[j-1]
    end = time.clock()
    LIS = max(S)
    return end - start, S

A = [7, 6, 5, 4, 3, 2, 1, 8, 3, 1, 4, 2, 3, 4, 7, 5, 0, 2]
A = map(int, A)


time, LIS_V = LIS(A)

print time, LIS_V
