#Loops - repeat instructions
#WAP to print hello for 5 times
print("hello")
print("hello")
print("hello")
print("hello")
print("hello")
     #or
a=100
print("hello\n"*a) 

#while loop - till the condition under while is true the programe will execute and when it becomes false the execution will stop.
while True:
    print("hello") #print hello infinite 

count = 1 #to kill variable we take a variable
while count <= 10:
    print("hello")
    count = count+1    #print 5 times hello
    print(count) #6

# 1 iteration = one complete cycle of loop
# iterator = example(count variable)
i = 1
while i <= 100:
    print("apnacollege", i)
    i += 1 #apnacollege 1 to apnacollege 100

#WAP to print number from 1 to 5
i = 1
while i<=5:
    print(i)
    i+=1

#WAP to reverse the loop
i=5
while i >= 1:
    print(i)
    i-=1 

#print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i+=1

#print number from 100 to 1
i = 100
while i >= 1:
    print(i)
    i-=1

#print multiplication table of number n
n=int(input("n : "))
i=1
while i <= 10:
    print(n,"*",i,"=",n*i)
    i+=1

#print the elements of the following list using a loop.
list = [1,4,9,16,25,36,49,64,81,100]
i=0
while i <= len(list)-1:
    print(list[i])
    i+=1 

#search for a number x in the tuple using loop.
tup = (1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i < len(tup):
    if(tup[i] == x):
        print("found at ind",i)
    i+=i














