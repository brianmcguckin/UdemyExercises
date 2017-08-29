#Test whether user input is valid
#if not return error message and ask again

print("Enter first side length: ")
lengthOne = 0   #defining variable to get to loop
while lengthOne <= 0:
    lengthOne = int(input())    #redefining variable to user's input
    if lengthOne >0:
        print("Enter second side length: ") #continue to next input
    else:
        print("Length cannot be zero or negative")
        print("Enter first side length: ")  #repeat input and re test value

lengthTwo = 0
while lengthTwo <=0:
    lengthTwo = int(input())
    if lengthTwo > 0:
        print("Enter final side length: ")
    else:
        print("Length cannot be zero or negative")
        print("Enter second side length: ")

lengthThree = 0
while lengthThree <=0:
    lengthThree = int(input())
    if lengthThree > 0:
        print("") #continue onto program here
    else:
        print("Length cannot be zero or negative")
        print("Enter final side length: ")
