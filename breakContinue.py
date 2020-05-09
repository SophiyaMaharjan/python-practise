'''largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

largestNumber = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end program: "))
    if number == -1:
        break
    counter += 1
    if number > largestNumber:
        largestNumber = number

if counter != 0:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

word = input("enter a word: ")
while word:
    word = input("enter a word: ")
    if word =="chupacabra":
        print("you have successfully left the loop.")
        break'''

word = input("enter a word: ")
word = word.upper()
wordWithoutVowels = ""
for letter in word:
    if letter == "A":
        continue
    elif letter =="E":
        continue
    elif letter=="I":
        continue
    elif letter=="O":
        continue
    elif letter=="U":
        continue
    wordWithoutVowels = wordWithoutVowels+letter
    pass
print(wordWithoutVowels)
 
 
