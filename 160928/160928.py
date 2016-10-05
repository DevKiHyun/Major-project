>>> a
'1'
>>> a = range(5)
>>> a
[0, 1, 2, 3, 4]
>>> a.append(10)
>>> a
[0, 1, 2, 3, 4, 10]
>>> a = range(2, 20 , 2)
>>> a
[2, 4, 6, 8, 10, 12, 14, 16, 18]

>>> a = [None]*5
>>> a
[None, None, None, None, None]
>>> a[1]
>>> a[1] = 100
>>> a
[None, 100, None, None, None]

>>> a = range(5)
>>> a = [None]*5
>>> a = [[1,2,3], [3,4,5]]
>>> a[0][0]
1
>>> a[0][1]
2
>>> import array
>>> a = array.array
>>> a = array.array('i', range(10))
>>> a
array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> import sys
>>> print sys.getsizeof(a)
96
>>> b = array.array('f', [3.14, 2.8])
>>> b
array('f', [3.140000104904175, 2.799999952316284])
>>> from array import *
>>> c = array( 'd', [3.14, 2.8])
>>> c
array('d', [3.14, 2.8])
>>> a = array('i')
>>> a.append(10)
>>> a.append(20)
>>> a
array('i', [10, 20])
>>> a.insert(1,30)
>>> a
array('i', [10, 30, 20])
>>> a = [1,2,3]
>>> t = (1,2,3)
>>> a
[1, 2, 3]
>>> t
(1, 2, 3)
>>> a[1]
2
>>> t[1]
2
>>> a[1] += 10
>>> a
[1, 12, 3]
>>> t[1]
2
>>> t[1] += 10

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t[1] += 10
TypeError: 'tuple' object does not support item assignment
>>> print ("tuple is imputable")
tuple is imputable
>>>
