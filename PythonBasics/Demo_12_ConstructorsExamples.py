"""

#Classes - user defined blueprint or prototype
# Classes will have variables and methods
#Constructor is called when object is created for class
#Constructor is like another method
#If no constructor is created by default constructor is called during run time
# init is the name used to create constructor in python, in java class name is used as constructor name
# __init__(self) method is known as constructor in OOps terminology. Its used to initialise objects state when its created
# init is automatically called when new instance of class is initialised
"""
class Calculator:
    # Variables created under clas are called class variables
    # class variables remains constant
    num = 100

    # default constructor
    def __init__(self):
        #Variables created inside constructor are called instant variables
        #instant variables are passed from class object creation
        #self is object reference when calling class methods or data, obj is passed as first parameter using self keyword
        print("Im called automatically when object is created")

    def getdata(self):
        print("I'm executing method inside class")


#call the class and no new keyword is used assign the class to object
obj = Calculator()
obj.getdata() # calling method
print(obj.num) #calling variable

