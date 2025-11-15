list1=[77,"hii","bye","hattt",456]

print(len(list1))
list2=[22,78,45,1002]
print(max(list2))
print(min(list2))
lst = [1, 2, 3]
lst.append(4)
print(lst)   # [1, 2, 3, 4]


lst = [1, 2, 3]
lst.insert(1, 100)  
print(lst)   # [1, 100, 2, 3]

lst = [1, 2, 3]
lst.extend([4, 5])
print(lst)   # [1, 2, 3, 4, 5]

lst = [10, 20, 30]
lst.remove(20)
print(lst)   # [10, 30]

lst = [10, 20, 30]
lst.pop()       # removes 30
lst.pop(0)      # removes 10
print(lst)

lst = [4, 1, 7, 2]
lst.sort()
print(lst)   # [1, 2, 4, 7]

lst = [1, 2, 3]
lst.reverse()
print(lst)   # [3, 2, 1]

lst = ["a", "b", "c"]
print(lst.index("b"))  # 1

lst = [1, 2, 2,2, 3]
print(lst.count(2))  # 2

lst = [1, 2, 3]
lst.clear()
print(lst)   # []

sum([1, 2, 3])  # 6

