#-*-coding: utf-8-*-

#sum(n) = 1+2+3+......+(n-1)+n
#sum(n) = sun(n-1) + n -> recursion(재귀식)

#recursion
def sum(n) :
    if n == 1:
        return 1
    return sum(n-1) + n
#T(n) = c + T(n-1) #점화식
#a(n) = a(n-1) + c -> T(1) = 1, a(1)= 1
#T(n) = T(n-1) + c = T(n-2) + c+c = T(n-3) + c + c + c =..= 1+ (n-1)c = O(n)
# 재귀식의 표현은 점화식으로 표현된다!

#sum(a,b) = a + (a+1) + ... + (a+b)/2 + [(a+b)/2 +1] + ... + (b-1) + b - ex) sum(n) = sum(1,n)
# => sum(a, (a+b)/2) + sum((a+b)/2+1 , b)

def sum(a,b) :
    if a == b :
        return a
    return sum(a, (a+b)/2) + sum((a+b)/2+1, b)

#T(a,b) = a에서 b까지 더하는 sum(a.b) 의 수행시간
#T(n) = n개의 연속된 정수의 합을 계산하는 sum(a,b) 의 수행시간 (b=a+1개의 합)
#T(n) = T(n/2) + T(n/2) + c = 2T(n/2) + c , T(1) = 1
#T(n) = 2T(n/2) + c = 2(2T(n/2^2) + c) + c = ... = 2^kT(n/2^k) + (2^(k-1) + x^(k-2) + .... 1)c
# n/2^k = 1 => n = 2^k => k =Log(2)n
#T(n) = 2^kT(1) + (2^(k-1) + 2^(k-2) + .. 2^1 + 2^0)c
#T(n) <= c(2^k) + (2^(k-1) + 2^(k-2) + .. 2^1 + 2^0)c
#= (2^0 + 2^1 + .. 2^(k-1) + 2^k)c = 2^0(2^(k+1)-1)/(2-1)c
#T(n) = (2^(k+1) -1)c -> 2^(k+1) = 2n
#T(n) = c2n- c = O(n)
