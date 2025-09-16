#Classes - user defined blueprint or prototype
# Classes will have variables and methods

class Calculator:
    num = 100

    def getdata(self):
        print("I'm executing method inside class")


#call the class and no new keyword is used assign the class to object
obj = Calculator()
obj.getdata() # calling method
print(obj.num) #calling variable

"""
#Constructor is called when object is created for class
#Constructor is like another method
#If no constructor is created by default constructor is called during run time
# init is the name used to create constructor in python, in java class name is used as constructor name
"""