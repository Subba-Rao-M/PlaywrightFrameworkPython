#Tuples Data Type
#Tuples is same like list but the difference is it is immutable means cannot update(List can be updated)
#Tuples are values are stored inside ()

values = (1, 2, 3.5, "Testing", 4, 5)

print(values[0])#1
print(values[3])#Testing
print(values[5])#5

#To print the last value in index
print(values[-1]) #5

# To print the sub list values
print(values[1:3])#(2, 3.5) 3 is not included as last value included is not considered

#values.insert(3, "Python Learning") #Insert is not allowed

#values.append("End of list") # append is not allowed

#values[4] = "Testing using Playwright" #Updating value at particular index is not allowed

#del values[0] - Deleting value at particular index is not allowed

person = ("Rahul", 25, 5.9)
print("Age: "+str(person[1]))