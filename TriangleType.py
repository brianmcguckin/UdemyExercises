#Write a function that accepts 3 sides of a triangle and returns the type
# of triangle
#Equilateral = all sides equal
#Isosceles = two sides are equal
#Scalene = no sides are equal

def checkType(lengthOne, lengthTwo, lengthThree):
    #check if side one is equal to another side
    if lengthOne == lengthTwo or lengthOne == lengthThree:
        #check if the remaining sides are equal
        if lengthTwo == lengthThree:
            return("Equilateral")
        #condition if only 2 sides are equal
        else:
            return("Isosceles")
    #check if sides two and three are equal
    elif lengthTwo == lengthThree:
        return("Isosceles")
    #if no sides are equal
    else:
        return("Scalene")

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
    triangleType = checkType(lengthOne, lengthTwo, lengthThree)
    if lengthThree > 0:
        print("Triangle type is: {}".format(triangleType))
    else:
        print("Length cannot be zero or negative")
        print("Enter final side length: ")
