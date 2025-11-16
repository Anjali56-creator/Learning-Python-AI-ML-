"""A dictionary (dict) is an unordered, mutable, and indexed collection where each item has a key and a value.

🧠 Key Points

Keys are unique (no duplicates allowed).

Values can be anything (numbers, strings, lists, other dictionaries).

Mutable → you can change, add, or remove items.

Indexed by keys, not by numbers like lists."""


student={
    "name":"Anjali",
    'city':"Patna",
    "rollnumber":53,
}
print(type(student))
print(type["name"])
print(student)

student={
    "name":"Anjali",
    'city':"Patna",
    "rollnumber":53,
    'name':"kumari"
}
print(student)


#updation and change
student["city"]="pune"
print(student)
student["favsubject"]="physics"
print(student)

# ALL DICTIONARY FUNCTIONS IN ONE CODE

d = {"name": "Anjali", "age": 19, "city": "Ghaziabad"}
print("Original Dictionary:", d)

# 1. keys()
print("\nKeys:", d.keys())

# 2. values()
print("Values:", d.values())

# 3. items()
print("Items:", d.items())

# 4. get()
print("Get name:", d.get("name"))
print("Get country (not present):", d.get("country"))

# 5. update()
d.update({"age": 20, "country": "India"})
print("\nAfter update:", d)

# 6. pop()
d.pop("country")
print("After pop(country):", d)

# 7. popitem()
d.popitem()
print("After popitem():", d)

# 8. setdefault()
d.setdefault("branch", "CSE")
print("After setdefault():", d)

# 9. copy()
d2 = d.copy()
print("Copy of dictionary:", d2)

# 10. clear()
d2.clear()
print("After clear() on copy:", d2)
