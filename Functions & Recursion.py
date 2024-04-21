#Functions-block of statements that can perform some specific task
#decrease redundency of code and increase reusability of codes.
#function defination
def cal_sum(parameter1, parameter2): #parameters
       sum = parameter1 + parameter2
       print(sum)
       return sum      
        
cal_sum(12, 6)  #function call ;arguments


def calc_sum(a, b):
       print(a+b)
       return a+b
calc_sum(12,16) #28
calc_sum(2,6) #8

#no parameter means function dont take any input
def print_hello(): 
       print("hello")

print_hello()

#WAP to create a fun which returns the avg oif three numbers
def calc_Avg(a, b, c):
       avg=(a+b+c)/3
       print(avg)
       return(avg)
calc_Avg(2,4,6)

#functions are of two types built-in and user defined
#built-in functions- already defined.Ex - print(),len(),type(),range()
print("neha", end=" ")
print("kumari")   #neha kumari

print("neha", end="*")
print("kumari") #neha*kumari

#user defined- Defined by user

#default parameters-asign values to parameter.if we dont pass an argument then finction will take default values to execute the code
def calc_prod(a, b=5):
       print(a*b)
       return a*b
calc_prod(1) #1*5

def calc_prod(b=3, a=5):
       print(a*b)
       return a*b
calc_prod(1) #1*5

#WAP to print length of a list(list is the parameter)
def List_Length(marks=[]): 
       print(len(marks))
       return len(marks)

List_Length(marks=[93,64,98,72,87,96]) #6

#WAP to print the element of a list in a single line.(list is the parameter).
def List_items(Item = []):
       print(Item)
       return Item
List_items(Item = ["salt","oil","sugar","wheat","rice"]) #['salt', 'oil', 'sugar', 'wheat', 'rice']



                         #RECURSION
#recursion-a a function call itself repeatedly.
def show(n):
       if(n==0): #basecase
           return
       print(n)
       show(n-1)

show(5)





