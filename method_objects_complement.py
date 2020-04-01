# chapter-3: object oriented programming and applications
# 3.2 method objects complement

'''
OOP
Organized programming structure which is object-focused
Program is divided into objects
Objects could represent 'real-world' objects or a broad category-classification of some entity. Example:
 - a bank account
 - a media item
 - a geometrical form
 - a mathmatical equation, etc.
Data objects and functions are now coupled together. Functions that belong to a particular class are called methods.
Methods can operate on the particular data object (offering some custom functionality)
'''
# CLASS
# A class is a template for creating objects. A class contains both data and methods declarations.
# Outline:


class Name:
    # constructor __init__ that defines the attributews for Name (these are instance variables)
    # various methods to operate the instance variables
    pass  # this class does nothing


# Example:
class Rectangle:

    # constructor for Rectangle class
    def __init__(self, width=0, height=0):
        self.w = width
        self.h = height

    # methods for Rectangle class
    def compute_area(self):
        return self.w*self.h

    def compute_perim(self):
        return (self.w+self.h)*2

# OBJECT
# Every object is an instance of some class.


'''
class Rectangle
    data: w, h
    methods: compute_area, compute_perim
'''

box1 = Rectangle(100, 100)  # object box1
box2 = Rectangle(200, 200)  # object box2

print("box1 area=", box1.compute_area())  # first instance
print("box2 perim=", box2.compute_perim())  # second instance

# DESIGNING NEW OBJECTS
# Let us write a new class representing a car
# We may want to define some attributes that describe the car (make, model, year)


class Car:
    # a simple attempt to represent a car

    # constructor
    def __init__(self, make, model, year, odometer=0):
        self.make = make
        self.model = model
        self.year = year
        # add a functionality that will be set to 0 as soon as the object Car is created
        self.odometer = odometer

    # an info method that returns a string description of the car
    def __str__(self):
        info = str(self.year)+" "+self.make+" "+self.model+" "+str(self.odometer)
        return info

    # add one method that will be able to increment the odometer and return some info
    def increment_odometer(self, miles):
        self.odometer = self.odometer + miles
        print("New odometer is "+str(self.odometer))


mycar1 = Car("Nissan", "Pathfinder", 2015, 32000)
mycar2 = Car("Ford", "Explorer", 2019)

print(mycar1)
mycar1.increment_odometer(1000)
print(mycar2)
mycar2.increment_odometer(2000)
