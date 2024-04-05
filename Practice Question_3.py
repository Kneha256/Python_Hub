#WAR to check if a number enter by the user is odd or even
number=int(input("Enter a number : "))
if(number%2==0):
    print("It is an even number")
else:
    print("It is an odd number") 


#WAP to find the greatest of 3 numbers entered by the user
num1=int(input("num1 : "))
num2=int(input("num2 : "))
num3=int(input("num3 : "))
if(num2<num1>num3):
    print("Greatest value is : ", num1)
if(num1<num2>num3):
    print("Greatest value is : ", (num2))
if(num1<num3>num2):
    print("Greatest value is : ", (num3))


#WAP to check if a number is a multiple of 7 or not
number=int(input("Enter a number : "))
if(number%7==0):
    print("yes")
else:
    print("No")


#practice
num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
if(num1%num2==0):
    print(str(num1 )+ " is divisible by " +str(num2))
else:
    print(str(num1 )+ " is not divisible by " +str(num2))
      #or
num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
if(num1%num2==0):
    print(num1, " is divisible by ",num2)
else:
    print(num1,+ " is not divisible by ",num2)