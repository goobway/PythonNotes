# NOTES FOR PYTHON 122 LECTURE JAN 29, 2020

def my_function_name(my_arguments):
    # block contains set of instructions
    return "some_value"

# simple function: no arguments or retun values
def sayhello():
    print("Hello")

sayhello()
sayhello()
print(type(sayhello))

# function with single argument
def greeting(name):
    print("Hello" + name)

# function with return statment
def greeting1(name):
    welcome="Hello " + name
    return welcome

greet=greeting1("chewbacca")
print(greet)
print(greeting1("Luke"))
print(greeting1("Leia"))

# remarks: welcome is a local function variable - not visible to the main program
# print(welcome) inside the main program, will return a Python error
# functions can also return the result of an expression

# function with return statement
def greeting2(name):
    return "Hello " + name

answer = input("What is your name? ")
greet2=greeting2(answer)
print(greet2)

answer = input("\nWhat is your name? ")
print(greeting2(answer))

# multiple functions, arguments and return statement
def greeting3(myname):
    return "Hello " + myname

def new_greeting(lname,lage):
    return greeting3(lname)+", you are"+lage

name=input("What is your name? ")
age=input("What is your age? ")
print("Hello " + name + ", you are " + age + " years old.")

# If global variables are needed, they can be declared at the very top of the file 
# (they will be visible everywhere and inside the functions)

# function with optional arguments and default values
def sayhello(name="Everybody"):
    print("Hello "+name)

sayhello("Luke")
sayhello()

# function with keyword arguments
def multiple_sum(a,b,c=0,d=0):
    return a-b+c-d

print(multiple_sum(2,1))
print(multiple_sum(a=2,b=1,d=3))
print(multiple_sum(d=3,b=1,a=2))