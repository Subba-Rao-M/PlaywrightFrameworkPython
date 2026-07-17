#List Data Type
#Similar to Arrays in java
#List allows multiple values with different data types
# List value are stored inside []
# lists are mutable means we can update the list values


values = [1, 2, 3.5, "Testing", 4, 5]
print(values[0])#1
print(values[3])#Testing
print(values[5])#5

#To print the last value in index
print(values[-1]) #5

# To print the sub list values
print(values[1:3])#[2, 3.5] 3 is not included as last value included is not considered

#To insert value at 3rd position and print values
values.insert(3, "Python Learning")
print(values) #[1, 2, 3.5, 'Python Learning', 'Testing', 4, 5]

#To add the value at the end of list, use append
values.append("End of list")
print(values)#[1, 2, 3.5, 'Python Learning', 'Testing', 4, 5, 'End of list']

# To update the value present in particular index
values[4] = "Testing using Playwright"
print(values)#[1, 2, 3.5, 'Python Learning', 'Testing using Playwright', 4, 5, 'End of list']

# To delete the values
del values[0]
print(values)#[2, 3.5, 'Python Learning', 'Testing using Playwright', 4, 5, 'End of list']

#To remove the last value
values.pop(1)
print("Pop usage")
print(values)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("First fruit: " + fruits[0])
print("Last fruit: " + fruits[-1])
print("Fruits from index 1 to 2: " + str(fruits[1:3]))