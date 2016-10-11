import sys
for i in range(0, int(raw_input())):
    A , B = raw_input().split()
    A = int(A)
    B = int(B)
    while A != 0 and B != 0 :
        if A > B :
            A = A % B
        else :
            B = B % A
    print(A+B)
