# A program that reads a sequence of numbers
'''# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# read the first number
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution
while number != 0:
    # check if the number is odd
    if number % 2 == 1:
        # increase the odd_numbers counter
        odd_numbers += 1
    else:
        # increase the even_numbers counter
        even_numbers += 1
    # read the next number
    number = int(input("Enter a number or type 0 to stop: "))

# print results
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

secret_number = 777
number = int(input("enter a number"))
while number!=secret_number:
    print("Ha ha! You're stuck in my loop")
    number = int(input("enter a number"))
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
blocks = int(input("Enter the number of blocks: "))
	
count = 0
height = 0
while count<blocks:
    height = height+1
    count= count+height
    if count>blocks:
        height = height-1

print("The height of the pyramid:", height)'''

number = int(input("enter a natural number except 1: "))
count = 0
while number !=1:
    if number%2 == 0:
        number = number/2
    else:
        number = 3*number + 1
    count +=1
    print(number)
print("iteration: ",count)
