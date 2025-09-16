#For loop Demo

obj=[2,3,5,7,9]

for i in obj:
    print(i)
print("End of loop")

# To print the list with multipled by 2
print("Multiply value by2 ")
for i in obj:
    print(i*2)
print("End of loop for *2")

# Sum of first 5 natural numbers 1+2+3+4+5 = 15
summation=0
for j in range(1,6): # 6 is not included considers until 5
    summation = summation+j
    print(j)
print(summation)

# Print the sum of even numbers
print("Sum of Even Numbers")
sumeven=0
for k in range(0,10, 2): # 2 is used to increase the numbers
    sumeven = sumeven+k
    print(k)
print(sumeven)

print("Use only limit and skip index")
for l in range(10): 
    print(l)# 0 to 9
