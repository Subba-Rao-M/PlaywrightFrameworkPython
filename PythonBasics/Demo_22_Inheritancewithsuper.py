class Parent:
    def greet(self):
        return "Hello user"


class Child(Parent):

# By default constructor will be called, if any argument needs to be passed explicitly define init constructor
    def __init__(self, title):
        self.title = title # used to instantiate class variables

    def greet(self):
        return super().greet()+" Good Morning from Child"+self.title

#super() is used with inheritance to access the parent classes methods and variables
c = Child("Python code")
c.greet()