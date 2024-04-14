#Loops - repeat instructions
#WHILE LOOPS
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

list = ["shreya", 4, "neha", True, "shristi"]
i = 0
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

tuple = ("shreya", 4, "neha", True, "shristi")
x = "neha"
i = 0
while i < len(tuple):
    if(tuple[i] == x):
        print("found at", i)
    else:
        print("finding")
    i+=1


#keywords - break and continue
#break-it will terminate the loop when encountered.
i = 1
while i<=5:
    print(i)
    if(i==3):
        break #terminate
    i+=1


#continue-terminate the execution of current iteration and continue the execution of the loop with next iteration.
i=0
while i<=10: #odd no
    if(i%2==0):
        i+=1
        continue #skip
    print(i)
    i+=1

i=0
while i<=5:
    if(i%2!=0):
        i+=1
        continue #skip
    print(i)
    i+=1




#FOR LOOP - use for sequential traversal.for traversing list, tuple, strings etc.
#having index.
list=[1,2,3]
for el in list:
    print(el)

string="apnacollege"
for char in string:
    print(char)

tuple=(1,"neha",True)
for val in tuple:
    print(val)


#for with else
list=[1,2,3]
for el in list:
    print(el)
else:
    print(end)


list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)

tuple=(1,4,9,16,25,36,49,64,81,100)
x=49
indx = 0
for el in tuple:
    if(el==x):
        print("found at",indx)
        indx+=1
else:
        print("finding")


#range()-gives a sequence of number, starting from 0 by default, and increment by 1 and stop before a specific number.
range(5) #return 0,1,2,3,4
#range(start?(0),stop(5),step?(1)) [? means optional]
seq = range(5)
for el in seq:
    print(el)
 
for el in range(5): #stop
    print(el)

for el in range(2, 5): #star, stop
    print(el)

for el in range(1, 10, 2): #star, stop, step
    print(el) #1,3,5,7,9

#WAP to print number from 1 to 100
for el in range(1, 100):
    print(el)

#WAP to write a number from 100 to 1
for el in range(100, 0, -1):
    print(el)
#or
i=100
while i >= 1:
    print(i)
    i-=1

#print multiplication table of n
num=int(input("enter a number :"))
for n in range(1, 10):
    print(num,"*",n,"=",num*n)

#pass statement- is a null statement  that does nothing. it is used as a placeholder for future.
for el in range(10): 
    pass
print("hello world")

