#Easy
#Write a program to create a dictionary with 5 key-value pairs
cubsInfield = {"Rizzo":"1B","Baez":"2B,SS,3B","Zobrist":"2B,SS","Russell":"2B,SS","Bryant":"3B"}
print(cubsInfield)

#Medium
#Update the value of a key
cubsInfield["Russell"] = "DL"
print(cubsInfield)

#Hard
#Copy this dictionary to another dictionary and clear the first dictionary
cubsInfieldCopy = cubsInfield.copy()
cubsInfield.clear()
print(cubsInfieldCopy)
print(cubsInfield)
