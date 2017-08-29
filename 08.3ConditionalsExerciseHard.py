#check if a number is divisible by 10 and 50
#check if number is also divisible by 30
print("Enter a number:")
number = int(input())
if number % 10 == 0 and number % 50 == 0:
    if number % 30 == 0:
        print("Number is divisible by 10,50, and 30")
    else:
        print("Number is divisible by 10 and 50 but not by 30")
