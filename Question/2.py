# Write a code to check whether a given number is a palindrome.
a=int(input("Enter a number: "))
if str(a)==str(a)[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
