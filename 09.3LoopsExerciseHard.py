#Hard
#Write a program to check if a given number is prime or not

#assign user input to variable
print("Enter a number: ")
primeTest = int(input())

#check if number is only divisible by 1 and itself
#divide number by all integers between 1 and number

for number in range(2,primeTest):
    if primeTest % number is 0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
