#WAP to ask user to enter names of their 3 fvrt movies & store them in a list.
movie_1 = input("enter first movie name : ")
movie_2 = input("enter second movie name : ")
movie_3 = input("enter third movie name : ")
list_movies = [movie_1,movie_2,movie_3]
print(list_movies)
      #or
movies=[]
movie_1 = input("enter first movie name : ")
movie_2 = input("enter second movie name : ")
movie_3 = input("enter third movie name : ")

movies.append(movie_1)
movies.append(movie_2)
movies.append(movie_3)
print(movies)

#WAP to ask for grocery items from the customer and make a list.
List = []
List.append(input("Enter Item 1 : "))
List.append(input("Enter Item 2 : "))
List.append(input("Enter Item 3 : "))
print(List)     #['rice', 'wheat', 'salt']



#WAP to check if a list contains palindrome of element.
list=[1,2,3,2,1]
list_copy=list.copy()
list_copy.reverse()

if(list_copy == list):
    print("palindrome")
else:
    print("not a palindrome") #palindrome


#WAP to count no. of student with "A" grade in the list.
tup=("C","D","A","A","B","B","A")
print(tup.count("A")) #3


#store the above in a list and sort from "A" to "D".
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)    #['A', 'A', 'A', 'B', 'B', 'C', 'D']