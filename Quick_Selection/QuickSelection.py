def quickSelect (A,k) :
    S, M , L = [],[],[]
    p = A[0]
    #A -> S,M,L

    for i in range(0,len(A)) :
        if A[i] < p : S.append(A[i])
        elif A[i] > p : L.append(A[i])
        else : M.append(A[i])
    if k <= len(S) : quickSelect(S,k)
    elif k > len(S) + len(M) : quickSelect(L, k-len(S)-len(M))
    else : print p


A = [1,2,4,5,1,25,1361,124]
k = 6
quickSelect(A,k)

#Bestcase input A -> S,M,L |S|,|L| ~ |A|/2
# T(B)(n) =T(B)(n/2) + cn
#-> T(n/2^k) +(1/2^2+ 1/2 + 1)cn
# = T(n/2^k) + (1/2^(k-1) + 1/2^(k-2) + ... 1/2 + 1)cn
# <= T(1) + (1 + 1/2 + ... 1/2^(k-1) + 1/2^k+ ...)cn
# =1 +2cn =O(n)
# warst case -> T(w)(n) = T(w)(n-1) + cn = (T(w)(n-2) + c(n-1)) + cn = ...=
# = T(w)(1) + c(2+3+...+n) <= c(1+2+3 +....+n) = cn(n+1)/2 = O(n^2)
