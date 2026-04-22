try:
    a = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")

except ValueError:
    print("An error occurred. Please enter a valid number.")