class MyClass:

    @classmethod
    def class_method(cls):
        #class method will not have access to self keyword
        #cannnot be used for run time variables
        return "Class"

    def instance_method(self):
        return "Instance"

obj = MyClass()
print(obj.instance_method())
print(MyClass.class_method()) # Can be called using class name without creating object for class