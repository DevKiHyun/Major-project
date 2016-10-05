Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a.append(10)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a.append(10)
NameError: name 'a' is not defined
>>> a

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b = 10
>>> a.append(10)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a.append(10)
NameError: name 'a' is not defined
>>> int a
SyntaxError: invalid syntax
>>> array a
SyntaxError: invalid syntax
>>> a[]
SyntaxError: invalid syntax
>>> a[];
SyntaxError: invalid syntax
>>> a[10]

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[10]
NameError: name 'a' is not defined
>>> a = '1'
>>> a.append(10)

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a.append(10)
AttributeError: 'str' object has no attribute 'append'
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
>>> = [None] *5
SyntaxError: invalid syntax
>>> a = [Nonr] *5

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a = [Nonr] *5
NameError: name 'Nonr' is not defined
>>> a = [None]*5
>>> a
[None, None, None, None, None]
>>> a[1]
>>> a[1] = 100
>>> a
[None, 100, None, None, None]
>>> b = range [5]

Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    b = range [5]
TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'
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
>>> print sys.getsizeof(a)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print sys.getsizeof(a)
NameError: name 'sys' is not defined
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
