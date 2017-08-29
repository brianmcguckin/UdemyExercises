#Medium
#Write a program to print the sum of odd numbers from 1 to 10
sum = 0
for number in range(1,11):
    if number % 2 != 0:
        sum = sum + number
print(sum)
