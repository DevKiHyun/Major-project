def Quick(A, first, last) :
    p = (A[(first + last) / 2][1])/(A[(first + last) / 2][0])
    left = first
    right = last

    while left <= right :
        while (A[left][1])/(A[left][0]) < p :
            left = left + 1
        while (A[right][1])/(A[right][0]) > p :
            right = right - 1
        if left <= right :
            A[left], A[right] = A[right], A[left]
            left = left + 1
            right = right - 1
    if first < right :
        Quick(A, first, right)
    if left < last :
        Quick(A, left, last)

def sum_I(I,X,a) : #caculate profit
    global MaxProfit
    global Y
    n = len(I)
    sum_p = 0
    for i in range(a+1) :
        sum_p = sum_p + X[i]*I[i][0]
    if sum_p >= MaxProfit :
        Y = X
        MaxProfit = sum_p
        return sum_p
    else :
        return sum_p

def stack_size(I,X) :
    n = len(I)
    size = 0
    for i in range(n):
        size = size + X[i]*I[i][1]
    return size

def knapsack_fractional(I,a,now_size):
    n = len(I)
    fract_pv = 0
    if a == n :
        return 0
    while now_size != 0 and a != n :
        if now_size >= I[a][1]:
            fract_pv = fract_pv + I[a][0]
            now_size = now_size - I[a][1]
            a = a + 1
            if a == n : break
        if 0 < now_size and now_size < I[a][1] :
            fract_pv = fract_pv + now_size*((I[a][0])/(I[a][1]))
            now_size = 0
            a = a + 1
            if a == n : break
        if now_size == 0 :
            return fract_pv
    return fract_pv


def knapsack(I,X,a,k) :
    global MaxProfit
    global Y
    n = len(I)
    p_v = sum_I(I,X,a)
    now_size = k - stack_size(I,X)

    if sum(X) == 0 and X == Y :
        if now_size >= I[a][1] :
            X[a] = 1
            p_v = sum_I(I,X,a)
            now_size = k - stack_size(I,X)
        else :
            X[a] = 0

    if a >= n-1 :
        X[a] = 0
        return MaxProfit

    elif X[a] == 1 :
        if now_size >= I[a+1][1] :
            X[a+1] = 1
            knapsack(I,X,a+1,k)
            X[a+1] = 0
        if MaxProfit < p_v + knapsack_fractional(I,a+1,now_size) :
            knapsack(I,X,a+1,k)
            X[a+1] = 0
        else :
            return MaxProfit

    elif X[a] == 0 :
        if now_size >= I[a+1][1] :
            X[a+1] = 1
            knapsack(I,X,a+1,k)
            X[a+1] = 0
        if MaxProfit < p_v + knapsack_fractional(I,a+1,now_size) :
            knapsack(I,X,a+1,k)
            X[a+1] = 0
        else :
            return MaxProfit
    if a == 0 and X[a] == 1 :
        X[a] = 0
        p_v = sum_I(I,X,a)
        now_size = k - stack_size(I,X)
        if MaxProfit < p_v + knapsack_fractional(I,a+1,now_size) :
            knapsack(I,X,a+1,k)
        else :
            return MaxProfit

k = raw_input()
k = float(k)
P = raw_input().split() #profit
S = raw_input().split() #size
P = map(float,P)
S = map(float,S)
n = len(P)
I = []

for i in range(n) :
    t = (P[i],S[i])
    I.append(t)
Quick(I,0,n-1)

global Y
global MaxProfit

X = [0]*len(I) # check 1 or 0
Y = [0]*len(I) # save maxprofit state
MaxProfit = 0

knapsack(I,X,0,k)
print MaxProfit
