#Dictionary and set practice questions
#Question-store values in a dictionary
dict={}
dict.update({"table":["a piece of furnitue", "list of fact and figures"]})
dict.update({"cat":"a small animal"})
print(dict)

      #or

dict = {
    "cat":"a small animal",
    "table":["a piece of furnitue", "list of fact and figures"]

}
print(dict)

#Question-total no of classes we need
subject={"python","java","cpp","python","javascript","java","python","java","cpp","c"}
print(len(subject)) #5

#Question - 
marks1=int(input("Marks : "))
marks2=int(input("Marks : "))
marks3=int(input("Marks : "))
dict={}
dict.update({"chem":marks1})
dict.update({"Maths":marks2})
dict.update({"phy":marks3})
print(dict) #{'chem': 6, 'Maths': 7, 'phy': 9}


#Question-store 9 and 9.0 in a set
set1={9,9.0}
print(set1) #{9}

set1={9,"9.0"}
print(set1) #{9, '9.0'}
  #or
values={
    ("phy", 9),
    ("chem", 9.0)
}
print(values)  #{('phy', 9), ('chem', 9.0)}




