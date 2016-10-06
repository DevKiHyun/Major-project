import time

def slow_power(a,n) :
    if n == 1 :
        return a
    elif n == 0 :
        return 1
    else :
        return a * slow_power(a,n-1)

def fast_power(a,n) :
    if n == 0 :
        return 1
    elif n%2 != 0 :
        if n == 1 :
            return a
        n1 = n/2 +1
        n2 = n/2
        return fast_power(a,n1) * fast_power(a,n2)
    else :
        return fast_power(a,n/2) * fast_power(a,n/2)

a = int(raw_input())
n = int(raw_input())

if (n < 0) :
    start = time.clock()
    print "1/%d = %.5f" %(slow_power(a,abs(n)), 1.0/slow_power(a,abs(n)))
    mid = time.clock()
    print "1/%d = %.5f" %(fast_power(a,abs(n)), 1.0/fast_power(a,abs(n)))
    end = time.clock()
else :
    start = time.clock()
    print slow_power(a,n)
    mid = time.clock()
    print fast_power(a,n)
    end = time.clock()
print "%f, %f" %(mid-start, end-mid)
