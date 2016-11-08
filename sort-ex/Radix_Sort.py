import time
import math

def Radix(A):
    start = time.clock()
    cnt = int(math.log10(max(A)))
    nRadixcompare = 0
    nRadixswap = 0
    n = len(A)
    i = 1
    for k in range(cnt+1) :
        zero, one, two, three, four, five, six, seven, eight, nine = [], [], [], [], [], [], [], [], [], []
        for j in range(n):
            nRadixcompare = nRadixcompare + 3
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
                    four.append(A[j])
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
                k = pow(10, i-1)
                nRadixcompare = nRadixcompare + 10
                N = A[j]%pow(10, i)

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
        i = i + 1
    end = time.clock()
    return (nRadixcompare, nRadixswap, end - start, A)

def check_sort(A):
    n = len(A)
    for i in range(1,n):
        if A[i-1] > A[i] : return False
    return True

in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)

a,b,c,arr = Radix(B)

print "Compare = %d Swap= %d  time= %f" % (a,b,c)
print check_sort(arr)
