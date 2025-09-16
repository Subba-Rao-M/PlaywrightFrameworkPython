#print readline using readline methods
#Readline reads single line
#ReadLines reads all lines and store it in list

file = open('demofile.txt') # if file in different directory, give complete path


for line in file.readlines():
    print(line)

file.close() # always close
