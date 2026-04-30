# Write a code to find the minimum among three given numbers.
a, b, c = map(int, input("Enter three numbers: ").split())
def find_minimum(a, b, c):
    return min(a, b, c)
print("The minimum number is:", find_minimum(a, b, c))