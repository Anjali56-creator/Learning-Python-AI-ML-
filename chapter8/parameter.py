#function with parameters
def average(a,b):
    averagevalue=(a+b)/2
    print(averagevalue)
#function calling with arugment
average(5,10)
average(7,10)
average(80,98)
average(2,4)    



#function with default parameters
def average(a=11,b=19):
    averagevalue=(a+b)/2
    print(averagevalue)
#function calling with arugment
average(5,10)
average(7,10)
average(80,98)
average()    