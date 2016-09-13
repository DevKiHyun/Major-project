#-*-coding: utf-8-*-
L = raw_input()
L = L.split()   #String 에서 . 을 사용하면 string 에 관련된 함수 사용가능
                #split() = whitespace 기준으로 분리해라
print(L)

#A = int(L[0])  #int(~) = ~ 를 정수형태로 바꾼다.
#B = int(L[1])

# <=>   A,B = int(L[0]) , int(L[1])

A , B = raw_input().split()

# <=> A = int(L[0])  #int(~) = ~ 를 정수형태로 바꾼다.
#    B = int(L[1])

# <=>   A,B = int(L[0]) , int(L[1])


print (A)
print (B)

C = A + B

print (C)

x,y = 3, 5
x,y = y ,x
print(x)
print(y)
