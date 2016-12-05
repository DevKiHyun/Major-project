def heapify(H,n,k):
    while 2*k + 1 < n:
        left = 2*k + 1
        right = 2*k + 2
        if H[k][1] > H[left][1] :
            m = left
        else :
            m = k
        if right < n and H[right][1] < H[m][1] :
            m = right
        if k != m :
            H[k], H[m] = H[m], H[k]
            k = m
        else : break

def make_heap(H):
    n = len(H)
    for k in range(n/2,-1,-1) :
        heapify(H,n,k)

def insert(H,t):
    H.append(t)

def extract_min(H):
    n = len(H)
    H[0] , H[n-1] = H[n-1], H[0]
    temp = H[n-1]
    if n-1 != 0 :
        del H[n-1]
        heapify(H,n-1,0)
    return temp

def huffman(F) :
    n = len(F)
    for i in range(n) :
        t = (i,F[i])
        insert(H,t)
    make_heap(H)

    for i in range(n, 2*n-1) :
        first_H , x = extract_min(H)
        second_H, y = extract_min(H)
        F = F + [0]
        F[i] = x + y
        t = (i, F[i])
        insert(H,t)

    sum_F = 0
    for i in range(n,2*n-1):
        sum_F = sum_F + F[i]

    print sum_F


H = []
F = raw_input().split()
F = map(int, F)

huffman(F)
