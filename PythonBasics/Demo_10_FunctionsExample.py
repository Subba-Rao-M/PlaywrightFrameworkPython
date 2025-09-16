# Function is a group of related statements which perform specific task

#Function Delcaration
def greetme():
    print("Good Morning")

    print("End of function")

#Call the function here
greetme()
print("Good Night")

#Parameterized function
def greetme(name):
    print("Good Morning "+name)
#Call the function here
greetme("Subba Rao")

#Print sum of 2 integers

def addintegers(a,b):
    print(a+b)

addintegers(2,3)


def addintegers(a,b,c):
    return a+b+c

print(addintegers(2,3, 10))