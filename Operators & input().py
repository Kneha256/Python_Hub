#operators
#1)arithmetic operators(+,-,*,/,//,%.**)-use in numerical operations
a,b=4,3

print(a+b)
print(a-b)
print(a**b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#2)Assignment operator(=,-=,+=,*=./=,//=,**=)-to assign a value

a=2
a+=10
print(a)
a-=1
print(a)
a//=2
print(a)
a/=2
print(a)
a*=4
print(a)
a**=4
print(a)

#3)Relational/comparison operator(==,!=,>,<,>=,<=) - give ans. in True or False
a,b=4,3

print(a>b)
print(a<b)
print(a!=b)
print(a==b)
print(a>=b)
print(a<=b)

#4)Logical operators(not,and,or)
a=True
b=False
print(a and b)
print(a or b)
print(not(a<b))
print(not a)

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

#input()
name=input("name : ")
age=int(input("age : "))
price=float(input("price : "))
