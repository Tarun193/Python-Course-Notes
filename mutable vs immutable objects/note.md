# Mutable vs Immutable Objects in python

**Note:** As I mentioned in my previous videos every thing in python is Object.

So, there are two types of objects in python ***mutable***( list, dict, set ) and ***immutable*** (int, float, string, tuple).

**Mutable:** The object which can be modified once created.

```python

>>> ls = [1,2,3,4,5]
>>> print(ls)
[1,2,3,4,5]

# as you can see i can modify the list.
>>> ls[3] = 8
>>> print(ls)
[1,2,3,8,5]

```

**Immutable:** The object which can not be modified once created. If we try to modify the object, it throws an error.

```python

>>> s = "Hello world"
>>> s[4] = 3

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s[4] = 3
TypeError: 'str' object does not support item assignment

```
