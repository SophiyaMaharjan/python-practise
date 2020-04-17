print("The itsy bitsy spider climbed up the waterspout.")
print() #is not completely empty; it prints empty line
print("Down came the rain and washed the spider out.")

'''backslash(\) has special meaning when used inside the string
it is called the escaped character \n represents new line.
'''
print("Down came the rain\nand washed the spider out.") 
'''
if you need a backslash in the sentence then we need to use double backslash
(\\) if not then it escapes the character
'''
print("\\") #gives error need to use \\ instead of single \

'''
it prints the sentences in one line and separates them
with white space on its own initiative
comma separates them into three different arguments
'''
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

'''
where the end="" argument is present the value is assigned there
'''
print("My name is", "Python.", end=" ")
print(" Python.")
print("Monty Python.")
# sep="-" argument separates each arguments by - sign
print("My", "name", "is", "Monty", "Python.", sep="-")
#separates with **** and adds ... in end then prints python in same line
print("Programming","Essentials","in",sep="***",end="...")
print("Python")

print("      *\n     * *\n    *   *\n   *     *\n  *       *\n *         *\n***       ***")

print("  *       *\n"*4," *********")
