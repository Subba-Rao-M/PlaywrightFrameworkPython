# Data Types
b, c, d = 2, 4.8, "Testing multiple variables"
print(b,c,d)

#print("value of b"+b) #TypeError: can only concatenate str (not "int") to str
# format method is used to pass the values to {} {} where value is passed to those 2 place holders
# Use below when concatinating 2 different data types
print("{} {}".format("Value of b is", b))

# for same data types can be done like below
x="Test"
y="Python"
print(x+"Concatinate with"+y)

# how to know the data type of variable
print(type(b))

## Different Data Types - Numeric(int, float, complex), String, Boolean, List, Tuple, Dictionaries

age, height, favorite_color = 25, 5.9, "blue"

print("Age: " + str(age) + " | Type: " + str(type(age)))
print("Height: " + str(height) + " | Type: " + str(type(height)))
print("Favorite Color: " + favorite_color + " | Type: " + str(type(favorite_color)))