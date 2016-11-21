def findSubsequence(A):
    LIS = [0]*len(A)
    for i in range (len(A)):
        max = -1
        for j in range(i):
            if A[i] > A[j] :
                if max == -1 or max < LIS[j] + 1 :
                    max = 1 + LIS[j]
        if max == -1 :
            max = 1;
        LIS[i] = max;

    result = -1
    index = -1
    for i in range(len(LIS)) :
        if result < LIS[i] :
            result = LIS[i]
            index = i

    path = str(A[index]) + " "
    res = result -1
    for i in range(index-1,-1,-1) :
        if LIS[i] == res:
            path = str(A[i]) + " " + path
            res = res - 1

    print "Longest Increasing subsequence: %d" %(result)
    print "Actial Element: " + path

A = raw_input().split()
A = map(int,A)

findSubsequence(A)
