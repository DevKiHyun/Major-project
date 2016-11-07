
def Radix(A):
    zero, one, two, three, four, five, six, seven, eight, nine = [], [], [], [], [], [], [], [], [], []
    cnt = 0
    n = len(A)
    i = 1
    print A[0]
    for j in range(n):
        if i == 1:
            if A[j] % 10 == 0 :
                zero.append(A[j])
            if A[j] % 10 == 1 :
                one.append(A[j])

    #A = zero + one + two + three + four + five + six + seven + eight + nine
    print A
    i = i + 1
    cnt = 0
in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)

Radix(B)
