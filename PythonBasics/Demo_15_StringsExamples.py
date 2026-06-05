str1 = "Testing using Playwright"

print(str1[1])#e

print(str1[3:12])#ting usin

#concatinate both strings

print(str1+" And Python")

#concatinate strings with other data type

number = 100
print("{} {}".format("Print the values "+str1,number))

# To check if substring is present in main string
str2 = "Playwright"
print(str2 in str1)

#splitting string
print(str1.split( ))#['Testing', 'using', 'Playwright']
print((str1.split( ))[0])#Testing


#trim
str3 = " Selenim Java "
print(str3.strip())#Selenim Java in place of trim strip is used
#lstrip and rstrip to remove only left or right spaces
print(str3.lstrip())#Selenim Java
print(str3.rstrip())# Selenim Java
