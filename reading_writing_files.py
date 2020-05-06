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

## ask user to input coefficient values
a=input("Enter value for a: ")
b=input("Enter value for b: ")
c=input("Enter value for c: ")

## display user equation
print("Equation is: (%s)x**2(%s)x+(%s)"%(a,b,c))