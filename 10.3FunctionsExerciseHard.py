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


print("Enter first length: ")
lengthOne = int(input())
print("Enter second length: ")
lengthTwo = int(input())
print("Enter third length: ")
lengthThree = int(input())
triangleType = checkType(lengthOne, lengthTwo, lengthThree)
print("Triangle type is: {}".format(triangleType))
