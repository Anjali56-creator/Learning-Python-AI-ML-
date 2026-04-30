# Write a code to find the sum of numbers divisible by 4.
# The code must allow the user to accept a number and add
#  it to the sum if it is divisible by 4. 
# It should continue accepting numbers as long as the user 
# wants to provide an input and should display the final sum.
a=int(input("Enter a number: "))
sum=0
while(a):
    if a%4==0:
        sum+=a
        a=a/10
print("The sum of numbers divisible by 4 is:", sum)