#WAF to print length of a list(list is the parameter)
list=["neha",7,2003,"python"]
def List_Length(list): 
       print(len(list))
List_Length(list) #4


marks=[93,64,98,72,87,96]
def List_Length(marks): 
       print(len(marks))
List_Length(marks) #6

city=["delhi","mumbai","chennai","bihar","jharkhand","odisa"]
def print_len(list):
      print(len(list))

print_len(city)


#WAF to print the element of a list in a single line.(list is the parameter).
grocery = ["salt","oil","sugar","wheat","rice"]
def List_items(list):
    for item in list:
       print(list, end=" ")
List_items(grocery) #['salt', 'oil', 'sugar', 'wheat', 'rice']


#WAP to find the factorial of n.(n is the parameter)
def calc_factorial(n):
    fact=1
    for el in range(1,n+1):
       fact*=el
       print(fact)
calc_factorial(5)

#WAP to convert USD to INR
USD_value=int(input("Enter USD value : "))
def converter(usd_value):
      rupees=usd_value*83
      print(usd_value,"USD =",rupees,"INR")
converter(USD_value)

#waf to take user  int input and if number is odd the return a string value "odd", otherwise "even".

n=int(input("Enter Number : "))
def Even_Odd(n):
     if(n%2==0):
          print("EVEN NUMBER")
     else:
          print("ODD NUMBER")

Even_Odd(n)

n=int(input("enter a num (1:100) : "))
def prime_num(n):
    if (n%n==0):
        print("prime")
    else:
        print("non prime")
prime_num(n)



list=[1,2,3,2,1]
lis1=list.copy()
lis1.reverse()
if(list==lis1):
    print("palindrome")
else:
    print("not a palindrome")


tup=("c","d","a","a","b","b","a")
print(tup.count("a"))
