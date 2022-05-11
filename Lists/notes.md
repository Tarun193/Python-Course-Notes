# Lists

In Python list is defined as collecton of `items`, then items can be of any type. Lists can be used to store large amount of data in a single variable. Lists are created using square brakets `[]`.

```python

>>> ls = [1, 2, 3, 4, 5]
>>> print(ls)
[1,2,3,4,5]

>>> print(type(ls))
<class 'list'>

# List with different items datatype.

>>> ls_1 = [1, 3.5, "Clown", True, 3j + 2]
>>> print(ls)
[1, 3.5, "Clown", True, 3j + 2]

# List containing another list.
>>> ls = [[1,23],45,7]
>>> print(ls)
[[1,23],45,7]

```

## List Indexing

here n is size of list.

Each element in the list has a unique index. index start from 0 and ends at n-1.
Python list also have negative indexing, -1 fro right most element and -n for left most element.

```python

# Index   0  1  2  3  4
>>> ls = [1, 2, 3, 4, 5]
#- index -5 -4 -3 -2 -1

>>> print(ls)
[1,2,3,4,5]

>>> print(ls[0],ls[-5])
1 1

>>> print(ls[-1])
5

```

## List Slicing

We can also  slice small part of list. i.e. sublist using list slicing by doing following.
`list[start index: ending index: jump]`, here element at ending index get excluded.

```python

# Index   0  1  2  3  4
>>> ls = [1, 2, 3, 4, 5]
#- index -5 -4 -3 -2 -1

>>> print(ls)
[1,2,3,4,5]

>>> print(ls[0:3])
[1, 2, 3]

>>> print(ls[-1:-3])
[4, 5]

>>> print(ls[0:5:2])
[1, 3, 5]

```

## In-built list functions

There are some built in functions in python, which can preform some usefull operation on list.

- `list.append(x)`
Add an item to the end of the list.

- `list1.extend(list2)`
Extend the list by appending all the items from the second list.

- `list.insert(i, x)`
Insert an item x at  given position i.

- `list.remove(x)`
Remove the first item from the list whose value is equal to x.If x is not found it raises an error.

- `list.pop()`
removes the last element from the list and returns it. If pass index to pop function it pops the element at given index, and returns the element.

- `list.clear()`
Remove all items from the list

- `list.count(x)`
Return the number of times x appears in the list.

- `list.sort()`
Sort the items of the list in place

- `list.reverse()`
Reverse the elements of the list in place.

- `list.index(x)`
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

**Note:** For information you can also refer to the python list documentation by clicking on link below.

[python List Documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
