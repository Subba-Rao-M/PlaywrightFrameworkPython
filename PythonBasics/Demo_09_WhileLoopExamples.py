#while loop when you dont know when to exit
#Use condition to exit based on true or false for condition

it=4
while it>1:
    if it!=3:
        print(it)
    it=it-1
print("Exit while loop")

print("Test break statement")
it1=4
while it1>1:
    if it1==3:
        break
    print(it1)
    it1=it1-1
print("Exit while loop")

print("Test continue statement")
it2=10
while it2>0:
    if it2==9:
        it2 = it2 - 1 # decrement should be done else it will go to infinite loop
        continue
    print(it2)
    it2=it2-1
print("Exit while loop")