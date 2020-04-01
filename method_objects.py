# chapter-3: object oriented programming and applications
# 3.1 method objects

'''
POP: Procedural Oriented Programming 
OOP: Object Oriented Programming
- Improve code reusability, readability, maintenance, extension

POP vs OOP
- With OOP, data objects and functions are now coupled together.
- Functions that belong to a particular class are now called "methods".
'''

# OOP Example
# class definition


class Rectangle:  # attributes are w and h
    def __init__(self, width=0, height=0):
        self.w = width
        self.h = height

    # methods for Rectangle class
    def compute_area(self):
        return self .w*self.h


# main Program
box1 = Rectangle(200, 100)
a = box1.compute_area()
print("area=", a)


# another rectangle example
class Rectangle2:

    # constructor for Rectangle2 class
    '''
    - width and height are local variables for the method
    - the attributes w, h are instance variables, they are shared within
    the entire class instance
    - w, h are accessible using the self dot operator
    '''

    def __init__(self, width=0, height=0):
        self.w = width
        self.h = height

    # mehtods for Rectangle2 class
    '''
    compute_area
    - method without local variables
    - method using a return value
    '''

    def compute_area(self):
        return self.w*self.h

    '''
    info
    - method without local variables
    - method without a retun value
    '''

    def info(self):
        print("w=%s; h=%s" % (self.w, self.h))

    '''
    scale
    - method with one local variable
    - method without a return value
    '''

    def scale(self, factor):
        self.w = self.w*factor
        self.h = self.h*factor


box2 = Rectangle2(100, 100)

box2.info()
a = box2.compute_area()
print("area=", a)

box2.scale(2)  # here box2 is 200x200
box2.info()
a = box2.compute_area()
print("new area=", a)

# displays area increasing with scale factor
for i in range(5):
    box2.scale(2)
    a = box2.compute_area()
    print("area=", a)


# another rectangle example (design change)
class Rectangle3:

    # constructor for Rectangle3 class
    def __init__(self, width=0, height=0):
        self.w = width
        self.h = height

    # methods for Rectangle3 class
    def compute_area(self):
        return self.w*self.h

    def info(self):
        print("w=%s; h=%s" % (self.w, self.h))

    '''
    - modify the method scale to become get_scaled_rectangle
    - no longer modifies the instance variables w, h
    - returns a new object of type Rectangle3. 
    - there are two steps combined: (i) instantiate and (ii) return
    '''

    def get_scaled_rectangle(self, factor):
        return Rectangle3(self.w*factor, self.h*factor)


# how does this change the for loop?
box3 = Rectangle3(100, 100)

for i in range(5):
    box = box3.get_scaled_rectangle(2)
    # to obtain the same output of previous for loop:
    # box = box3.get_scaled_rectangle(2**(i+1))
    a = box.compute_area()
    print("area=", a)


# condensing the for loop
for i in range(5):
    print("area=", box3.get_scaled_rectangle(2**(i+1)).compute_area())


'''
Can we "print" an object?
In python, it is possible to call the str function on any native types: int, boolean, list, etc. 
- Examples:
s1=str(2)   s2=str(3.4)   s3=str(False)   s4=str([3,4,5])
and then print(s1,s2,s3,s4)
- We could also just do: print(2,3.4,False,[3,4,5]) because it implicitly calls the str function for us
- It is sometimes useful for a new class that we create to be able to return its "string value"
- This value could be anything we want it to be
'''

# For example, for the class Rectangle we had the info method:


def info(self):
    print("w=%s; h=%s" % (self.w, self.h))

# We are going to instead call this method __str__


def __str__(self):
    return "w=%s;h=%s" % (self.w, self.h)
# We will now be able to print the object of type Rectangle the same way we print any other variables


class Rectangle4:
    # constructor for Rectangle4 class
    def __init__(self, width=0, height=0):
        self.w = width
        self.h = height

    # methods for Rectangle4 class
    def compute_area(self):
        return self.w*self.h

    def __str__(self):
        return "w=%s; h=%s" % (self.w, self.h)

    def get_scaled_rectangle(self, factor):
        return Rectangle4(self.w*factor, self.h*factor)

box4 = Rectangle4(100,100)
print("mybox"+str(box4))
print("mybox",box4)

for i in range(5):
    print(box4.get_scaled_rectangle(2**(i+1)))
