for i in range(0, int(raw_input())):
    A , B = int(raw_input().split())
    while A != 0 and B != 0 :
        if A > B :
            A = A % B
        else :
            B = B % A
    print("gcd =", A+B)
