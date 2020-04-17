# Testing TypeError message
'''input gives result as string the code below gives an error
if needed a number from input function as a result we need to convert string into
numbers we can do it by type casting'''

#anything = input("Enter a number: ") #gives result in string
anything = int(input("Enter a number: ")) #using type casting converts result into integer
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

# + sign concatinates two strings
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

x = float(input("Enter value for x: "))

a = x+1/x
print(a)
b = x+1/a
print(b)
c = x+1/b
print(c)
y=1/c

print("y =", y)

