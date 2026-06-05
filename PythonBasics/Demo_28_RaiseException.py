person = ("Rahul", 25, 5.9)
print(person[1])
try:
    person[0] = "Subba"
except Exception as e:
    print(e)
    print("Since tuple is immutable cannot modify the data")