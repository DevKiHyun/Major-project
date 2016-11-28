import time

def LIS(A) :
    start = time.clock()
    i = 0
    min_element = min(A)
    min_loca = 0
    worst_cnt = 0
    worst = 0
    check_cnt = 0

    while A[i] != min_element :
        min_loca = min_loca + 1
        i = i + 1

    for i in range(0, min_loca + 1) :
        if A[i] == min_element:
            worst_cnt = worst_cnt + 1
            break
        if A[i+1] < A[i] :
            worst_cnt = worst_cnt + 1

    if worst_cnt == min_loca + 1 :
        worst = 1

    if worst == 1:
        S = [1]*worst_cnt + [0]*(len(A)-worst_cnt)
        if worst_cnt == len(A) :
            S = [1]*len(A)
        else :
            for j in range(worst_cnt , len(A)) :
                temp = A[j]
                i = j
                if A[j] < A[j-1] :
                    while temp > A[i] :
                        i = i - 1
                    S[j] = S[i] + 1
                else :
                    S[j] = S[j-1] + 1
    elif worst == 0:
        S = [1]*1 + [0]*(len(A)-1)
        for j in range(1,len(A)):
            temp = A[j]
            i = j-1
            '''
            if j-2 != 0 and S[j-1] < S[j-2] :
                k = j-2
                while temp <= A[k] :
                    if k == 0:
                        break
                    k = j - 1
                if k == 0 :
                    S[j] = S[k]
                else :
                    S[j] = S[k] + 1
            '''
            if A[j] < A[j-1] :
                while temp <= A[i] :
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
    print S
    return  LIS


#A = raw_input().split()
A = [3 ,5 ,2 ,1 ,4 ,5 ,6 ,2 ,7 ,5 ,8 ,9 ]
#in_file = open('LIS.txt', 'r')
#A = list(in_file.read().split())
A = map(int, A)

print A
LIS_V = LIS(A)

print  LIS_V
