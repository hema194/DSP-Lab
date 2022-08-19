Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 16:30:00) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d={}
>>> type(d)
<class 'dict'>
>>> d={"name":"Hema","ID NO":404}
>>> type(d)
<class 'dict'>
>>> d1=dict()
>>> type(d1)
<class 'dict'>
>>> d2=dict+([(1,2),(3,4)])

>>> d2=dict([(1,2),(3,4)])
>>> type(d2)
<class 'dict'>
>>> print(d2)
{1: 2, 3: 4}
>>> #dic modification:
>>> d["ID NO"]=403
>>> print(d)
{'name': 'Hema', 'ID NO': 403}
>>> #adding element:
>>> d["contact no"]=7286023194
>>> print(d)
{'name': 'Hema', 'ID NO': 403, 'contact no': 7286023194}
>>> #delete element:
>>> del(d["contact no"])
>>> print(d)
{'name': 'Hema', 'ID NO': 403}
>>> #delete by using pop():
>>> d.pop()

>>> d.pop("ID NO")
403
>>> print(d)
{'name': 'Hema'}
>>> d.popitem()
('name', 'Hema')
>>> print(d)
{}
>>> d.popitem(d2)

>>> d2.popitem()
(3, 4)
>>> print(d2)
{1: 2}
>>> #rectriving elements:
>>> #keys
>>> d3={1:"a",2:"b",3:"c",4:"d"}
>>> d3.keys()
dict_keys([1, 2, 3, 4])
>>> #values
>>> d3.values()
dict_values(['a', 'b', 'c', 'd'])
>>> #items
>>> d3.items()
dict_items([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')])
>>> #getting element:
>>> d3.get(d3["c"])

>>> d3.get(d3[3])
>>> print(d3)
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
>>> d3.get(3)
'c'
>>> help(d3)

>>> d3.update(1:"aaa")
SyntaxError: invalid syntax
>>> d3.update([1:"aaa"])
SyntaxError: invalid syntax
>>> d3.update([1,"aaa"])

>>> d3.update({1:"aaa"})
>>> print(d3)
{1: 'aaa', 2: 'b', 3: 'c', 4: 'd'}
>>> d2.clear()
>>> print(d2)
{}
>>> #copy:
>>> d2.copy(d3)

>>> d2=d3.copy()
>>> print(d2)
{1: 'aaa', 2: 'b', 3: 'c', 4: 'd'}
>>> 