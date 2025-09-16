#access properties of parent from child
#child will have access to parent without creating new variables and methods
from Demo_13_InstantVariablesExamples import Calculator


class ChildClass(Calculator):
    print("Inside Child class")
    num2 = 200

    #IF parent constructor is not using default constructor , explicitly create constructor and call base class constructor

    def __init__(self):
        Calculator.__init__(self, 10, 20)
        print("Init child class")

    def getcompletedata(self):
        return self.num2 + self.num+ self.firstNumber+ self.secondNumber

#Child classes
obj = ChildClass()
print(obj.num)
print(obj.getcompletedata())
