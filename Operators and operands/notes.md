# Operators and Operands

operators perform operations on operands. `2 + 3` in this `2` and `3` are operands and `+` is operator which will perform addition operation on the operands.
this `2 + 3` Whole is called expression.

## Types of Operators

- Arithmetic Operators
- Assignment Operators
- Relational Operators
- Logical Operators
- Membership Operator
- Identity Operator

### Arithmetic Operators

this include all mathematical operations. i.e. +, -, /, *, %, **
, //

```python

>>> 2 + 3 # addition
5
>>> 10 - 5 # subtraction
5
>>> 5/2 # simple division
2.5
>>> 5 // 2 # floor division(gives integer value)
2
>>> 5 % 3 # gives reminder
2
>>> 2 ** 3 # 2 to the power 3
8
>>> 4 * 5 # multiplication
20

```

### Assignment Operators

`=` is assignment Operator. It is used to assign values to variables.
we can use the assignment operator with arithmetic operators as given below.

```python

>>> x = 10 # assigning 10 to x
>>> print(x)
10
>>> x += 3 # x += 3 is same as x = x + 3
>>> print(x)
13
>>> x -= 3  # x -= 3 is same as x = x - 3
>>> print(x)
10
>>> x /= 2 # x /= 3 is same as x = x / 3
>>> print(x)
5.0
>>> x *= 2 # x *= 3 is same as x = x * 3
>>> print(x)
10.0

# Similarly we can do these with %, // , ** operators.
```

### Relational Operators

Relation Operator returns boolean values. It gives the relation between two variables. `x > y` this will return `True` if `x` is greater than `y`, else `False`

Relational operators are: <, >, >=,<=, ==, !=.

```python

>>> 2 > 3 # is 2 greater than 3
False
>>> 2 < 3 # is 2 lesser than 3
True
>>> 2 <= 2 # is 2 less than equal to 2
True
>>> 3 >= 4 # is 2 greater than equal to 4
False
>>> 4 == 4 # is 4 equal to 4.
True
>>> 2 == 3 # is 2 equal to 3.
False
>>> 2 != 3 # is 2 not equal to 3.
True

```

### Logical Operators

Logical operators are used to combine two or more relation expressions to form complex experssions.

Logical operators are: and, or, not

- `and`  - return `True` if both expressions are `True` i.e. `True and True`. else `False`
i.e. `False and True`,`True and False`,`False and False`

- `or` - return `True` if even one expressions is `True` i.e. `True and True`,`False and True`,`True and False`. else `False`,i.e. `False and False`

- `not` - return opposite i.e. `not True` = `False`

```python

>>> 2 > 3 and 2 < 3
False
>>> 2 > 3 or 2 < 3
True
>>> not 2 > 3
True

```

### Membership operator

it use to check whether a given sequence contains the other sequence. `in` is membership operator.

```python

>>> "ll" in "hello"
True
>>> "aa" not in "hello"
True

```

### Identity Operator

It Checks whether two operands have same identity or not. `is` is identity operator.

```python

>>> a = 5
>>> b  = a # now a and b are pointing to same value 5 or same object.So they will have same id.

>>> a is b
True

```
