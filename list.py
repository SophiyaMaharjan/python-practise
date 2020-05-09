'''numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers) # printing original list content

numbers[0] = 111
print("New list content: ", numbers) # current list content

numbers[1] = numbers[4] # copying value of the fifth element to the second
print("New list content:", numbers) # printing current list content

print("\nList's length:", len(numbers)) # printing previous list length

###

del numbers[1] # removing the second element from the list
print("New list's length:", len(numbers)) # printing new list length
print("\nNew list content:", numbers) # printing current list content


numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

## reverse the element in the list or can write just myList.reverse
myList = [10, 1, 8, 3, 5]
length = len(myList)

for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append('John Lennon')
beatles.append('Paul McCatney')
beatles.append('George Harrison')
print("Step 2:", beatles)

# step 3
for i in range(2):
    name = input("enter a band member : ")
    beatles.append(name)
    i+=1
    pass
print("Step 3:", beatles)

# step 4
del beatles[-2]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0, 'Riingo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

# can sort the list using listName.sort()
myList = [8, 10, 6, 2, 4] # list to sort

for j in range(len(myList)):
    for i in range(len(myList) - 1): # we need (5 - 1) comparisons
        if myList[i] > myList[i + 1]: # compare adjacent elements
            # if we end up below it means that we have to swap the elements
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
print(myList)


myList = [8, 10, 6, 2, 4]        
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)'''

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []
newList.append(myList[0])
length = len(myList)
for i in range(length):
    if myList[i] not in newList:
        newList.append(myList[i])
    pass

print("The list with unique elements only:")
print(newList)
