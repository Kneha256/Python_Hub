#if-elif-else or if or if-elif (Syntax)
Light=input("Light : ")
if(Light == "red"):
    print("Stop")
elif(Light == "green"):
    print("Go")
elif(Light == "yellow"):
    print("Look")
else:
    print("Broken")


Marks=int(input("Enter your Marks : "))
if(Marks>=90):
    print("Grade : A")
elif(Marks<=90 and Marks>=80):
    print("Grade : B")
elif(Marks<=80 and Marks>=70):
    print("Grade : C")
else:
    print("Grade : D")


#if-elif-else
food=input("food : ")
if(food=="cake" or food=="jalebi"):
    print("sweet")
else:
    print("no sweets")
