#LISTs-it is a built-in data type that stroes set of values.
#in list indexing start with 0 always.
#it can store elements of different data types. 
#but in an array only one type of data can be store.

marks=[12.4, 15.4, 13.2, 6.9, 18.5]
print(marks)  #[12.4, 15.4, 13.2, 6.9, 18.5]
print(type(marks))  #list
print(marks[4]) #18.5
print(marks[0]) #12.4
marks[4]=12.0
print(marks) #[12.4, 15.4, 13.2, 6.9, 12.0]
print(len(marks)) #5


#String is immutable - values can be only be accessed but cannot change.
str="neha"
print(str[0])
str[0]="k"
print(str) #give error
      #but in case of list
#list are mutable - values can be change of any particular object.
arr=["neha",5,"aman",4]
arr[1]=7
print(arr) #['neha', 7, 'aman', 4]
print(arr[5]) #error



#List Slicing - access a part of list or sublist.
#name_list[starting_index:ending_index] ending index is not included
L1=[12,30,14,18,22]
print(L1[0:4]) #[12, 30, 14, 18]
print(L1[:4]) #[12, 30, 14, 18]
print(L1[1:]) #[30, 14, 18, 22]
print(L1[ : ]) #[12, 30, 14, 18, 22]

#Negative list_slicing
print(L1[-4:-1]) #[30, 14, 18]
print(L1[-4:]) #[30, 14, 18, 22]



#List Methods
#1)append method - adding something at the end
list = [2,1,3]
list.append(8)
print(list)

#2)sort method - sorts in accending order
list = [2,1,3]
print(list.sort()) #none because it is making change in original value
print(list) #[1,2,3]

list = [2,1,3]
print(list.append(4)) #none
print(list.sort()) #none
print(list) #[1,2,3,4]

list = ["banana", "cake", "apple" ,"rose"]
print(list.sort()) #none
print(list)  #['apple', 'banana', 'cake', 'rose']

#3)sort(reverse=Ture) gives sorted list in decending order.
list = [2,1,3]
print(list.sort(reverse=True)) #none because it is making change in original value
print(list) #[3,2,1]

list = ["banana", "cake", "apple" ,"rose"]
list.sort(reverse=True)
print(list)  #['rose', 'cake', 'banana', 'apple']


#4)reverse method - reverse the list(inside main list or variable)
list1=["banana", "cake", "apple" ,"rose"]
list1.reverse()
print(list1) #['rose', 'apple', 'cake', 'banana']

list2=['c','f','a','k','j']
list2.reverse()
print(list2) #['j', 'k', 'a', 'f', 'c']

#5)insert method- similar to append method but it can insert value at any index.
#list_name(idx, el)
list = ["banana", "cake", "apple" ,"rose"]
list.insert(3, "cherry")
print(list) #['banana', 'cake', 'apple', 'cherry', 'rose']

list1=[2,3,1]
list1.insert(2, 5)
print(list1) #[2, 3, 5, 1]

#6)remove method - remove first occurance of element
list=[1,4,6,4]
list.remove(4)
print(list) #[1, 6, 4]

list = ["banana", "rose", "apple" ,"rose"]
list.remove("rose")
print(list) #['banana', 'apple', 'rose']

#7)pop method - remove value from a particular index.
list=[1,8,6,4]
list.pop(3)
print(list) #[1, 8, 6]

list = ["banana", "jasmine", "apple" ,"rose"]
list.pop(3)
print(list) #['banana', 'jasmine', 'apple']


                           #TUPLE

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