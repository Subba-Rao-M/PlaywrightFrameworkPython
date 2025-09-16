str = "Testing using Playwright"

print(str[1])#e

print(str[3:12])#ting usin

#concatinate both strings

print(str+" And Python")

#concatinate strings with other data type

number = 100
print("{} {}".format("Print the values "+str,number))

# To check if substring is present in main string
str2 = "Playwright"
print(str2 in str)

#splitting string
print(str.split( ))#['Testing', 'using', 'Playwright']
print((str.split( ))[0])#Testing


#trim
str3 = " Selenim Java "
print(str3.strip())#Selenim Java in place of trim strip is used
#lstrip and rstrip to remove only left or right spaces
print(str3.lstrip())#Selenim Java
print(str3.rstrip())# Selenim Java
