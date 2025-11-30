def square(num=10):
    return num**2

print(square(2)) 


#write a function that takes a string and return the count of vowels and consonant separetely
def func(userInput):
    vowels = "aeiouAEIOU"
    countvowels = 0
    countconsonants = 0
    for eachchar in userInput:
        if eachchar.isalpha():
            if eachchar in vowels:
                countvowels += 1
            else:
                countconsonants += 1
    return countvowels, countconsonants   

vowels, consonants = func("anjali")
print(vowels, consonants)
