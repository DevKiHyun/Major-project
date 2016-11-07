import time

def Bubble(A):
    start = time.clock()
    nBubble_compare = 0
    nBubble_swap = 0
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            nBubble_compare = nBubble_compare + 1
            if A[j-1] > A[j] :
                nBubble_swap = nBubble_swap + 1
                A[j-1], A[j] = A[j], A[j-1]
    end = time.clock()
    print A
    return nBubble_compare, nBubble_swap, end-start

in_file = open('sort.txt', 'r')
B = list(in_file.read().split())
B = map(int, B)

print B

a,b,c = Bubble(B)
print "Compare = %d Swap= %d  time= %f" % (a,b,c)
