# Variables and Basic Datatypes

**note:** Each and everthing in python is an object.

`print()` Function is used to produced output on the screen.

```python
>>> print("hello World")
'Hello world'
```

## Variables

A variables is like a container that stores values(information) you can access or change.
The purpose variable is to store the information so that we can preform task on the stored information later.

### Rules for declearing variable

All variable names must begin with a letter of the alphabet or an
underscore( _ ).  For beginning programmers, it may be easier to begin all variable names with a letter of the alphabet.

 After the first initial letter, variable names can also contain letters and numbers.  No spaces or special characters, however, are allowed.

 Uppercase characters are distinct from lowercase characters. In other words variable are case sensitive.

## Datatpyes

Basic Data types in python:

- Integer
- Float
- Complex
- Boolean
- None
- string (Sequence)

In python we do not need to specify the datatype of the variable. i.e We don't need to specify that what value that variable is going to store as we have to do in statically typed programming languages such as C and C++.

We can spimply do

```python

# here a is my variable and 5 is the value which I assinged to it and you can see there is no need of mention that a is going to store integer.

>>> a = 5 # data of integer type
>>> a = 5.0 # data of float type

>>> 3j + 5 # Complex number

# boolean datatype have only two objects
>>> True
>>> False

# string object
>>> "Hello g"
```

We can get type of the object with help of `type` Function.

```python

# <class 'int'> means 1 is an object of integer class. In other words it is an integer value and similar with other types of data.
>>> type(1)
<class 'int'>

>>> type(3.34e3)
<class 'float'>

>>> type(True)
<class 'bool'>

>>> type("Tarun")
<class 'str'>

>>> type(2j+1)
<class 'complex'>

```
