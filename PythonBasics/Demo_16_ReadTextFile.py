file = open('demofile.txt') # if file in different directory, give complete path
#print(file.read())  # to read all contents
#print(file.read(8))  # to read n number of characters

# to read one single line completely
print(file.readline())# to read the line completely #abc
print(file.readline()) #bcd

#print readline using readline methods

file.close() # always close
