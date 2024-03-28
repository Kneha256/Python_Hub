#String store a sequence of character(a char, a word, a para or a sentence).
#different ways to create string
str1 = "this is a string"
str1 = 'this is a string'
str1 = """this ia a string"""
txt1 = "this is neha's brother"
txt1 = 'this is neha"s brother'

#escape sequence characters (tab(\t), next line(\n))
str1 = "this is a string. we are creating it in python"
str1 = "this is a string. \nwe are creating it in python" #print in next line
str1 = "this is a string. \twe are creating it in python" #for a tab space

#Basic operation on String
#concatenation(+)
str1="Apna"
str2="College"
print(str1+str2)
print(str1+" "+str2)

#length of str (len())
str1="Apna College" #it counts a single space as a character
print(len(str1))

str1="Apna"
str2="College"
final_str=str1+" "+str2
print(final_str) #Apna College
print(len(final_str)) #12


#indexing - when we declare a string then a specific no is alot to each char and indexing start with 0 always.
#use to access charachters
#<varname>[index no]

str1="Apna_college"
print(str1[3]) #a

#or

str1="Apna_college"
ch= str1[4] #_
print(ch)

#Slicing - to access part of a string 
#str[start_index:ending_idx] ending index is not included
str1="ApnaCollege"
print(str1[1:5]) #pnaC

print(str1[0:5]) #ApnaC
   #or
print(str1[:5]) #ApnaC

print(str1[4: ]) #College
   #or
print(str1[4:len(str1)]) #College

print(str1[0:4]) #Apna

#slicing in Negative indexing - last char is -1 index.no then 2nd last is -2 index.no and so on
#<var>[first index:last index]
#same is positive sliccing last index no will not be added
str1="Apple"
print(str1[-3:-1]) #pl
print(str1[-3:]) #ple
print(str1[-5:]) #Apple

#String Function
#str.endswith - return Ture if string ends with substring
st="I am a intelligent person"
print(st.endswith("son")) #Ture
print(st.endswith("per")) #False

#str.capitalize() - it gives first character of a string in capital letter
#to give the output it creat a new string and there is no change in original string
#it will work once only
str1="i am a intelligent person"
print(str1.capitalize()) #I am a intelligent person
print(str1) #i am a intelligent person
 
   #but is we want permanent change then

str1="i am a intelligent person"
str1=str1.capitalize() 
print(str1) #I am a intelligent person






            

