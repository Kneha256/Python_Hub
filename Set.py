#set is the collection of unordered items and stores only values (not as key:value of dict).
#set is mutable(new elemnt cand be add and old can be remove) but elements are immutable.
#each set must be unique inside the set and immutable(can not be changed).
#list and dictionary can not be store inside set because they are mutable.
#we can use tupble, string, float , integer and boolean values only.
collection={2,3,4,6}
print(collection)   #{2, 3, 4, 6}
print(type(collection))   #<class 'set'>

#all type of values can be taken.
collection={2,2,2,3,4,6,"hello",True}
print(collection) #{True, 2, 3, 4, 6, 'hello'}

#it ignores duplicate values.
collection={2,2,2,"hello","world","world"}
print(collection) #{2, 'hello', 'world'}

#length will also ignore duplicate values.
collection={2,2,2,"hello","world","world"}
print(len(collection)) #3

#to create an empty sets we need to write "set()".
collection = {} #will create dict

collection = set() #empty set syntax
print(type(collection)) #<class 'set'>

#Set Methods
#1)add method - to add an element(set_name.add(el))
collection={2,2,2,"hello","world","world"}
collection.add("neha")
print(collection) #{2, 'hello', 'neha', 'world'}

number=set() #add function with empty set
number.add(1)
number.add(2)
number.add(3)
print(number) #{1, 2, 3}

number=set() #trying to add a tuple
number.add(1)
number.add(2)
number.add((4,"neha","abhi"))
print(number)   #{(4, 'neha', 'abhi'), 1, 2}

number=set() #trying to add a list
number.add(1)
number.add(2)
number.add((4,"neha","abhi"))
number.add([4,"neha","abhi"])
print(number)  #TypeError:unhashable type: 'list
#when we will add any immutable type it will not through any error
#because immutable types have some hash value when we perform any add operation will list there are chances to get changes in its hash value becuase list is mutable.
#hashable means immutable.

#2)set.remove(el) - remove the element
collection={2,2,2,"hello","world","world"}
collection.remove("hello")
print(collection) #{2, 'world'}

#3)set.clear() - #empetise the set
collection={2,2,2,"hello","world","world"}
collection.clear()
print(collection) #set()

#4)set.pop() - pop any random value
collection={2,2,2,"hello","world","world"}
collection.pop()
print(collection) #randomly pop(give) any element.
#if we try to remove 7 which is not present in the set then it will give an error(keyerror: 7)

#5)set.union(set2) #combine both set values and return new
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2)) #{1, 2, 3, 4, 5}

#6)set.intersection(set2) #combine common values and return new
set1={1,2,3}
set2={3,2,5}
print(set1.intersection(set2)) #{2, 3}



