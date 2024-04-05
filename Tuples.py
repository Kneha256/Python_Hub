#Tuple is a built-in data type which is immutable 
tup = (2,4,7,5,9)
print(type(tup)) #<class 'tuple'>
print(tup[0]) #2
tup[0]=10 #not allowed


#to create a single value tuple
tup1=(4,)
print(tup1) 
#for multiple values
tup1=(3,6,64,93,)
       #or
tup1=(3,6,64,93) #same

#slicing in tuple
tup1 = (2,4,7,5,9)
print(tup1[0:3])  #(2, 4, 7) last index is included
print(tup1[1:]) #(4, 7, 5, 9)
print(tup1[:4]) #(2, 4, 7, 5)

#negative sslicing
print(tup1[-3:-1]) #(7, 5)
print(tup1[-4:]) #(4, 7, 5, 9)


#tuples Method
#1)index method - return index of first occurance
#tup_name(el)
tup1 = (2,4,7,5,7)
print(tup1.index(7)) #2

#2)count method - return counts of total occurance
tup1 = (2,4,7,5,7)
print(tup1.count(7)) #2