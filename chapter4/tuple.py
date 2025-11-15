"""A tuple is a collection of items that is:

Ordered

Indexed

Allows duplicate values

Immutable (you cannot change it after creation)

Tuple is written using parentheses ( )."""

t = (10, 20, 30)
print(t)
"""t = (10, 20, 30)
t[1] = 50   # ❌ ERROR"""
t = ("apple", "banana", "cherry")
print(t[0])   # apple
print(t[-1])  # cherry

t = (1, 2, 2, 3)
print(t.count(2))   # 2

t = ("a", "b", "c")
print(t.index("b"))   # 1

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # (1, 2, 3, 4)

t = (1, 2)
print(t * 3)   # (1, 2, 1, 2, 1, 2)

lst = [10, 20, 30]
print(tuple(lst))   # (10, 20, 30)

emptytuple=()
print(emptytuple)
