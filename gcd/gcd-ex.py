import sys

f = open('gcd.txt')

for i in range(0,int(f.readline())):
    L = f.readline().split()
    A = int(L[0])
    B = int(L[1])
    while A != 0 and B != 0:
        if A > B :
            A = A % B
        else :
            B = B % A
    print(A+B)
