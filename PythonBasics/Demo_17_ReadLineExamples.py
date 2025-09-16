#print readline using readline methods

file = open('demofile.txt') # if file in different directory, give complete path

line = file.readline()
while line!="":
    print(line)
    line=file.readline()
file.close() # always close
