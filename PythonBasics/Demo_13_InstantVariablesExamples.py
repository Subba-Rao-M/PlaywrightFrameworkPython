class Calculator:
     # class variables
    num = 100

    # Customized constructor
    def __init__(self, a, b):
        #Instant variables
        self.firstNumber = a
        self.secondNumber = b
        #self is object reference when calling class methods or data, obj is passed as first parameter using self keyword
        # self keyword is class instance reference
        print("Instance variables created")

    def getdata(self):
        print("I'm executing method inside class")

    def summation(self):
        # for calling class variable can use self or classname
        # for instant variables always use self keyword
        # for methods also self can be used if same method is used in parent and child, own class method can be used with self
        return self.firstNumber+self.secondNumber+Calculator.num

#call the class and no new keyword is used assign the class to object
obj = Calculator(10,20)
obj.getdata() # calling method
print(obj.num) #calling variable
print(obj.summation())

#Verify instance variables for another object creation
obj = Calculator(50,20)
print(obj.summation())