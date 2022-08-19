Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 16:30:00) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s={1,2,3,4,5,6,7}
>>> s1={"apple","orange","banana"}
>>> print(type(s))
<class 'set'>
>>> help(s)

>>> s.union(s1)
{1, 2, 3, 4, 5, 6, 7, 'banana', 'apple', 'orange'}
>>> s.intersection(s1)
set()
>>> s1={"apple","orange","banana"}
>>> s2={"a","b","orange"}
>>> s1.intersection(s2)
{'orange'}
>>> s1.difference(s2)
{'apple', 'banana'}
>>> s2.difference(s1)
{'b', 'a'}
>>> s3={a}
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s3={a}
NameError: name 'a' is not defined
>>> s3={"a"}
>>> s3.issuperset(s2)
False
>>> s2.issuperset(s3)
True
>>> s3.issubset(s2)
True
>>> 