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
    return end - start, LIS

in_file = open('LIS.txt', 'r')
A = list(in_file.read().split())
A = map(int, A)


time, LIS_V = LIS(A)

print time, LIS_V
