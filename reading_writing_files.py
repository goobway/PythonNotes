# chapter-3: object oriented programming and applications
# 3.3 more on i/o - reading/writing files

'''
I/O Review
Why do we need inputs?
 - obtain information from the user 
 - initalize (set) some data

 Why do we need outputs?
 - return information to the user
 - get computed data values

 In programming:
 - gathering the input is the preprocessing stage
 - computing is the processing stage
 - managing and returning the output is the postprocessing stage
'''

# funtions input and print
# print can be used to display info on screen
# input can be used to display some info and prompt the user to enter a string
print("Quadratic Equation f(x)=ax**2+bx+c")

# ask user to input coefficient values
a = input("Enter value for a: ")
b = input("Enter value for b: ")
c = input("Enter value for c: ")

# display user equation
print("Equation is: (%s)x**2(%s)x+(%s)" % (a, b, c))


# I/O REVISITED
'''
Input can be obtained in many different ways:
 - from the keyboard
 - from command-line argument
 - from a GUI
Output can be provided:
 - as text on a screen
 - by writing in a file
 - as graphics that will be displayed in a window
Python offers some useful objects and methods that ease the way we can handle I/O
'''

# INPUT FROM THE KEYBOARD
'''
First let us learn about the split() method
 - it is a method from the class str (acts on String objects)
 - it is used to separate (split) a given string into a list of strings
 - it can identifiy any delimiters/separators
'''
phrase = "Welcome to ECE 122"
mylist = phrase.split()  # split() uses blank separator as default
print(mylist)

phrase = "Welcome, to, ECE, 122"
mylist = phrase.split(", ")
print(mylist)

# second, let us learn about a trick for splitting list
i1, i2, i3, i4 = ["Welcome", "to", "New", "York"]
print(i1,i2,i3,i4)
