# Id and keywords

## `id` function

id() is a built-in function in Python 3, which returns the identity of an object. This is also the address of the object in memory. The identity is a unique integer for that object during its lifetime.

```python

>>> a = 5
>>> id(a)
1971253373328

>>> b = 5
>>> id(b)
1971253373328

```

Now, here `1971253373328` is identity of variable `a` which contains an **integer** object and we can see id of `a` and `b` is same, Which means both `a` and `b` are pointing to same location in memory.

```python

>>> a = 5 # integer object.
>>> id(a) 
1971253373328

>>> b = 5.0 # floating point object.
>>> id(b)
1971294094352

```

Now, here we can see both have different ids because both contains different objects.

## keywords

Keywords are words which have pre-defined specific meaning for the interpreter, they can not we used as the variable names. There are 36 keywords in python

For displaying keywords in python we can write the following code

```python

import keyword
print(keyword.kwlist)

```

### Output

```python
# list all the keywords.
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```
