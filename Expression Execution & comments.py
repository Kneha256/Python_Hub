#String and numeric values can operate together with *
#Repeat the string value as the numeric value is.
a,b = 4,6
c = "@"
print(a*b*c)

a,b = 2,2
c = "Hello"
print(a*b*c)

#String with string can operate with +
#concatenation
a,b="2",3
c="@"
print((a+c)*b)

a,b="hello",3
c="World"
print((a+c)*b)

#numeric values can opperate with all operatiors
a,b=2,3
c=4
print(a+b*c)

#Arithemetic expression with int and float will give float value
a,b=2,5.0
c=a*b
print(c)
    #or
a,b=2,5.0
print(a*b)
