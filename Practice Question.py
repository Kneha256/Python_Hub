num1=int(input("Enter First number : "))
num2=int(input("Enter second number : "))
print("sum = ",num1+num2)

side=float(input("Enter length of a side : "))
area=side*side #or area=side**2
print(area)

num1=float(input("num1 : "))
num2=float(input("num2 : "))
average=(num1+num2)/2
print(average)

a=int(input("num1 = "))
b=int(input("num2 = "))
print("True") if a>=b else print("False")
        #or
a=int(input("num1 = "))
b=int(input("num2 = "))
c=("False", "True") [a>=b]
print(c)


#string practice question
#Question01
first_name=input("Enter your first name : ") #neha
print(len(first_name)) #4

#Question02-write a programe to give the no of occurance of "$"
str = "I am learning python from $shraddha mam"
print(str.count("$")) #1

str1="apna college"
print(len(str1)) #12
print(str1[2]) #n
print(str1[1:6]) #pna c
print(str1[-11:-6]) #pna c


#string functions practice
str = "i am learning python from shraddha mam"
print(str.endswith("am")) #True
print(str.capitalize()) #I am learning python from shraddha mam
print(str.replace("mam", "khapra")) #i am learning python from shraddha khapra
print(str.find("from")) #21
print(str.count("a")) #5
