# read two numbers
'''number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# print the result
print("The larger number is:", larger_number)


# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# print the result
print("The larger number is:", larger_number) 

# read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# we check if the second number is larger than current largest_number
# and update largest_number if needed
if number2 > largest_number:
    largest_number = number2

# we check if the third number is larger than current largest_number
# and update largest_number if needed
if number3 > largest_number:
    largest_number = number3

# print the result
print("The largest number is:", largest_number)

stmt = input("enter a word ")
if stmt == 'Spathiphyllum':
    print("Yes - Spathiphyllum is the best plant ever!")
elif stmt == 'spathiphyllum':
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not [input]!")

income = float(input("Enter the annual income: "))
if income<=85528:
    a = (18/100)*income
    tax = a-556.2
    
else:
    b = income-85528
    a = (32/100)*b
    tax = a+14839.2
if tax<0:
        tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")'''

year = int(input("Enter a year: "))
if year>1582:
    if year%4 != 0:
        print('common year')
    elif year%100!=0:
        print('leap year')
    elif year%400 !=0:
        print('common year')
    else:
        print('leap year')
else:
    print("not within Georgian Calender")
