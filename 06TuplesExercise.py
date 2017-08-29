#Easy
#Write a program to create a tuple of 4 elements
parksTuple = ("Wrigley Field","Fenway Park","Camden Yards","Petco Park")
print(parksTuple)

#Medium
#Convert this tuple into a list
parksList = list(parksTuple)
print(parksList)

#Hard
#Delete the first element in this list and convert it back to a tuple
parksList.remove("Wrigley Field")
parksTuple = tuple(parksList)
print(parksTuple)
