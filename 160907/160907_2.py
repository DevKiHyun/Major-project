#-*-coding: utf-8-*-

a = [2, 9 , -1 , 4]

a[0] = 'apple'

a.append['banana']

a[-1]
a[-3]

b = a[1:3]  #1부터 2까지 slice

b = a[:3]

b = a[0:4:2] # 매 2칸씩 slice

if 'banana' in a:
    print 'I am not happy'

del a[1] # delete a[1]

a.remove[apple] #search 'apple' ande delete

c = a+b #concatenate

c.pop() # pop!
c.pop(0) # c[0] pop

for i in c:
    print i

# for C, for (i = 0; i < 10; i++)

for i in range(10):
    print i

# for C, for (i = 0; i < 10; i++) {print("%d\n",i);}


 a = [ 9,3, 1, 10, 21, 4 ,-8 ,2]

 a.sort # sort a

 b = [4,3,2,1]

 c = sorted.b

 import sys # sys 라는 모듈을 사용하겠다.

 a = []

 print sys.getsizeof(a)
 
