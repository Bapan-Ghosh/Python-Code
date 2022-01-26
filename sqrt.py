Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> math.sqrt(5.)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    math.sqrt(5.)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(5)
2.23606797749979
.
>>> import math as m
>>> m.sqrt(22)
4.69041575982343
>>> 