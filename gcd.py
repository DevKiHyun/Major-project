#-*-coding: utf-8-*-
L = raw_input().split()
A = int(L[0])
B = int(L[1])

while A != 0 and B != 0: #[while 조건문 :] 형식
    if A > B :
        A = A % B
    else :
        B = B % A
print ("gcd=", A+B)
