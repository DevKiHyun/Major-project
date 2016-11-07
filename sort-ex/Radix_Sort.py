import time

def Radix(A):
    start = time.clock()
    nRadixcompare = 0
    nRadixswap = 0
    cnt = 0
    n = len(A)
    i = 1
    while (1) :
        zero, one, two, three, four, five, six, seven, eight, nine = [], [], [], [], [], [], [], [], [], []
        for j in range(n):
            nRadixcompare = nRadixcompare + 4
            if i == 1 :
                nRadixcompare = nRadixcompare + 10
                if A[j] % 10 == 0 :
                    zero.append(A[j])
                elif A[j] % 10 == 1 :
                    one.append(A[j])
                elif A[j] % 10 == 2 :
                    two.append(A[j])
                elif A[j] % 10 == 3 :
                    three.append(A[j])
                elif A[j] % 10 == 4 :
                    tour.append(A[j])
                elif A[j] % 10 == 5 :
                    five.append(A[j])
                elif A[j] % 10 == 6 :
                    six.append(A[j])
                elif A[j] % 10 == 7 :
                    seven.append(A[j])
                elif A[j] % 10 == 8 :
                    eight.append(A[j])
                elif A[j] % 10 == 9 :
                    nine.append(A[j])

            else :
                k = pow(10, i)

                nRadixcompare = nRadixcompare + 11

                if  A[j] / k == 0:
                    cnt = cnt + 1
                N = A[j]%pow(10, i+1)

                if N / k == 0 :
                    zero.append(A[j])
                if N / k == 1 :
                    one.append(A[j])
                if N / k == 2 :
                    two.append(A[j])
                if N / k == 3 :
                    three.append(A[j])
                if N / k == 4 :
                    four.append(A[j])
                if N / k == 5 :
                    five.append(A[j])
                if N / k == 6 :
                    six.append(A[j])
                if N / k == 7 :
                    seven.append(A[j])
                if N / k == 8 :
                    eight.append(A[j])
                if N / k == 9 :
                    nine.append(A[j])
        A = zero + one + two + three + four + five + six + seven + eight + nine
        if cnt == n :
            end = time.clock()
            print A
            return (nRadixcompare, nRadixswap, end - start)
        i = i + 1
        cnt = 0


in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)
print B

a,b,c = Radix(B)

print "Compare = %d Swap= %d  time= %f" % (a,b,c)
