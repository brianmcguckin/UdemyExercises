#write a function that accepts two parameters and returns their secondNumber

def sum(numberOne, numberTwo):
     return(numberOne + numberTwo)


print("Enter first number: ")
numberOne = int(input())
print("Enter second number: ")
numberTwo = int(input())
numberSum = sum(numberOne, numberTwo)
print("Sum of numbers is: {}".format(numberSum))
