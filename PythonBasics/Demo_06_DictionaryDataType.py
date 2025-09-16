#Dictionary Data Type
#Similar to hashmap in java
#Data is stored in key value pair inside {key: value}
#Key can be number or string, if string enter value inside ""
#IF value is string "" and number

dictValue = {"a":1, 2:"b", 3:"Test", "last":99}
print(dictValue)#{'a': 1, 2: 'b', 3: 'Test', 'last': 99}
print(dictValue["last"])#99
print(dictValue[2])#b # here dont use " use how it is declared in dictionary

# Creating dictionary at run time
# create empty dictionary and then add values to it
dicEmp = {}
dicEmp["FirstName"] = "Subba"
dicEmp["LastName"] = "Rao"
dicEmp["EmpID"] = 1001
dicEmp["Salary"] = 50000
print(dicEmp)#{'FirstName': 'Subba', 'LastName': 'Rao', 'EmpID': 1001, 'Salary': 50000}

car = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
}

# Print the value associated with the 'model' key
print("Car model:", car["model"])

# Add a new key 'owner' with value 'Rahul'
car["owner"] = "Rahul"

# Print the updated dictionary
print("Updated car dictionary:", car)