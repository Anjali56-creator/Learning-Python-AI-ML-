items={"paneer","gulab","sandwitches","paneer"}
print(type(items))
print(items)

#it is mutable

# ALL IMPORTANT SET FUNCTIONS IN ONE CODE

s = {10, 20, 30, 40}
print("Original Set:", s)

# 1. add()
s.add(50)
print("\nAfter add(50):", s)

# 2. update()  → add multiple items
s.update([60, 70])
print("After update([60, 70]):", s)

# 3. remove()  → removes item (error if not present)
s.remove(20)
print("After remove(20):", s)

# 4. discard() → removes item (no error if not present)
s.discard(100)
print("After discard(100):", s)

# 5. pop() → removes a random element
removed = s.pop()
print("Pop removed:", removed)
print("After pop():", s)

# 6. clear() → empty the set
temp = s.copy()
temp.clear()
print("After clear():", temp)

# 7. copy() → shallow copy
new_set = s.copy()
print("Copy of set:", new_set)

# -------------------------------
#       SET OPERATIONS
# -------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 8. union()
print("\nUnion:", A.union(B))

# 9. intersection()
print("Intersection:", A.intersection(B))

# 10. difference()
print("Difference A-B:", A.difference(B))

# 11. symmetric_difference()
print("Symmetric Difference:", A.symmetric_difference(B))

# 12. issubset()
print("A issubset B:", A.issubset(B))

# 13. issuperset()
print("A issuperset B:", A.issuperset(B))

# 14. isdisjoint()
print("A isdisjoint B:", A.isdisjoint({10, 20}))
