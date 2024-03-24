#operators
#1)arithmetic operators(+,-,*,/,//,%.**)-use in numerical operations
a,b=2,3
print(a+b)

a,b=2,3
print(a-b)

a,b=2,3
print(a**b)

a,b=13,6
print(13//6)

#2)Assignment operator(=,-=,+=,*=./=,//=,**=)-to assign a value
a=2
print(a)
a+=2
print(a)

#3)Relational/comparison operator(==,!=,>,<,>=,<=) - give ans. in True or False
a,b=4,3
print(a>b)

a,b=4,3
print(a!=b)

i=6
print(i==5)

#4)Logical operators(not,and,or)
a=True
b=False
print(a and b)
print(a or b)

#5)identity operators(is,is not)=answer in true or false
a=True
b=False
print(a is b)

a=3
b=5
print(a is not b)


#6)Membership operator(in, not in)
list=(3,67,23,2,5,8)
print(3 in list)
print(5 not in list)

#7)bitwise operators(&,|,^)-work with bits(0,1)
print(0&1)
print(0|1)
print(0|3)
print(3^4)

#input() statement is used to take inpute values
#string input - words, setences
name = input("name : ")

#float input - decimal value
price = float(input("price : "))

#int input - number
age=int(input("age : "))

name = input("name : ")
print("my name is :",name,"and i'm",age,"years old")

