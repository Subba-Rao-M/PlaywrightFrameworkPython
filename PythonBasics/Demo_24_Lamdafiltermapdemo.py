"""
A lamda function in python is small anonymous function
can have multiple arguments but single expression
it is written in single line
it is used where short function required temporarily
dont use lambda if the function is complex, instead use def funciton

"""

def add(x, y):
    return x+y

sum1 = lambda x, y : x+y

"""
map -> modify the values present in list with new logic
filter - > filter tha data from list based on condition
"""

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda x: x*2, numbers)
print(list(squared_numbers)) # convert raw values to list

even_numbers = list(filter(lambda  x: x%2 == 0, numbers))
print(even_numbers)

print(sorted(numbers))# to sort the list data