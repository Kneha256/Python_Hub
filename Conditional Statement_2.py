#single line if / ternary operator
#<var>=<var> if [condition] else [condition]

food=input("food : ")
eat="yes" if food == "cake" else "no"
print(eat)

#<stt1> if <condition> else <stt2>
food=input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("no sweet")

      #or

#if-elif-else
food=input("food : ")
if(food=="cake" or food=="jalebi"):
    print("sweet")
else:
    print("no sweets")


#clever if / ternary operator
age=int(input("age : "))
vote=("yes", "no") [age<18]
print(vote)

sal=float(input("salary : "))
tax=sal*(0.1, 0.2) [sal>=50000]
print(tax)
