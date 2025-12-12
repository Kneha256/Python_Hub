#if-elif-else or if or if-elif (Syntax)
#"elif" condition will only execute if "if" condition is false.
#there can be number of if and elif statement but only one else statement.
#indentation-proper spacing



Light=input("Light : ")
if(Light == "red"):
    print("Stop")
elif(Light == "green"):
    print("Go")
elif(Light == "yellow"):
    print("Look")
else:
    print("Broken")


marks=int(input("Enter your marks : "))
if(marks >= 90):
     print("Grade : A")
if(marks >= 80 and marks < 90):
    print("Grade : B")
if(marks >= 70 and marks <80):
    print("Grade : C")    
else:
    print("Grade : D")


     #or



Marks=int(input("Enter your Marks : "))
if(Marks>=90):
    print("Grade : A")
elif(90>Marks>=80):
     print("Grade : B")
elif(80>Marks>=70):
    print("Grade : C")
else:
    print("Grade : D")




Marks=int(input("Enter your Marks : "))
if(Marks>=90):
    print("Grade : A")
elif(Marks<90 and Marks>=80):
    print("Grade : B")
elif(Marks<80 and Marks>=70):
    print("Grade : C")
else:
    print("Grade : D")

       #or

Marks=int(input("Enter your Marks : "))
if(Marks>=90):
    print("Grade : A")
if(Marks<90 and Marks>=80):
    print("Grade : B")
if(Marks<80 and Marks>=70):
    print("Grade : C")
else:
    print("Grade : D")



#if-elif-else
food=input("food : ")
if(food=="cake" or food=="jalebi"):
    print("sweet")
else:
    print("no sweets")



#nesting - one statement inside another
age = 34
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can Drive")
else:
    print("cannot Drive")
    






