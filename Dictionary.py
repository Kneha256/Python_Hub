#built-in and use to store data values in key(word):value(meaning) pairs.
#mutable-key:value scan be change, do not allow duplicate keys. 
#unordered - no index number is there.
''' dict = { "keys" : "values",
              "cgpa" : 9.6,
              "marks : [98, 86, 74],
              12.99 : 99.6
                          } '''

info = {
    "key" : "values",
    "name" : "neha",
    "roll_no" : 51,
    "age" : 21
    }
print(info)

#all types values are acceptable in dictionary.
#all data types are accaptable in values.
#list and dictionary are not allowed in key because these are mutable.
info = {
    "key" : "values",
    "name" : "neha",
    "marks" : 21.4,
    "age" : 21,
    "is_adult" : True,
    }
print(info)

#we can store list and tuples in dictionary as well.
info = {
    "key" : "values",
    "name" : "neha",
    "subjects" : ["python", "cpp", "java"], #list
    "topics" : ("dict","set"), #tuple
    "marks" : 21.4,
    "age" : 21,
    "is_adult" : True
    }
print(info) 
#output- {'key': 'values', 'name': 'neha', 'subjects': ['python', 'cpp', 'java'], 'topics': ('dict', 'set'), 'marks': 21.4, 'age': 21, 'is_adult': True}
print(type(info)) #<class 'dict'>
print(list(info)) #['key', 'name', 'subjects', 'topics', 'marks', 'age', 'is_adult']
print(tuple(info)) #('key', 'name', 'subjects', 'topics', 'marks', 'age', 'is_adult')


#to access a values in dictionary
#print(dict_name["keys"])
info = {
    "key" : "values",
    "name" : "neha",
    "subjects" : ["python", "cpp", "java"], #list
    "topics" : ("dict","set"), #tuple
    "marks" : 21.4,
    "age" : 21,
    "is_adult" : True
    }
print(info) 
print(info["name"]) #neha
print(info["topics"]) #('dict', 'set')
print(info["marks"]) #21.4
print(info["surname"]) #error
print(info["subjects"]) #['python', 'cpp', 'java']

#to change the value of a key
#dict_name["key"] = "value"
info["name"] = "aman"
print(info)

#to add a new key: value pair
info["name"] = "aman"
info["surname"] = "sinha"
print(info) #{'key': 'values', 'name': 'aman', 'subjects': ['python', 'cpp', 'java'], 'topics': ('dict', 'set'), 'marks': 21.4, 'age': 21, 'is_adult': True, 'surname': 'sinha'}


info["name"] = "aman"
info["name"] = "rohit" #overwrite old value instead of creating a new key value pair
info["surname"] = "sinha"
print(info) #{'key': 'values', 'name': 'rohit', 'subjects': ['python', 'cpp', 'java'], 'topics': ('dict', 'set'), 'marks': 21.4, 'age': 21, 'is_adult': True, 'surname': 'sinha'}

#empty dictionary
null_dict = {} #{}
null_dict["name"] = "neha" 
print(null_dict) #{'name': 'neha'}

#NESTED DICTIONARY
student = { "name" : "neha",
              "cgpa" : 9.6,
              "marks" : {
                  "PHY" : 98,
                  "CHEM" : 87,
                  "MATHS" : 90
                }
    }
print(student)
#output - {'keys': 'values', 'cgpa': 9.6, 'marks': {'phy': 98, 'chem': 87, 'maths': 90}}
print(student["name"]) #neha
print(student["marks"]) #{'PHY': 98, 'CHEM': 87, 'MATHS': 90}
print(student["marks"]["CHEM"]) #87
print(list(student["marks"])) #['PHY', 'CHEM', 'MATHS']


#DICTIONARY METHODS 
#1)dic_name.keys() - returns all outer keys.
student = { "name" : "neha",
              "cgpa" : 9.6,
              "marks" : {
                  "PHY" : 98,
                  "CHEM" : 87,
                  "MATHS" : 90
                }
    }
print(student.keys()) #dict_keys(['name', 'cgpa', 'marks'])
print(list(student.keys())) #return values keys in list formate
print(len(list(student.keys()))) #3

#2)dic_name.values() - return all values including inner dictionary.
student = { "name" : "neha",
              "cgpa" : 9.6,
              "marks" : {
                  "PHY" : 98,
                  "CHEM" : 87,
                  "MATHS" : 90
                }
    }
print(student.values()) #dict_values(['neha', 9.6, {'PHY': 98, 'CHEM': 87, 'MATHS': 90}])

#3)dic_name.items() - returns all (key,val)pairs as tuple.
student = { "name" : "neha",
              "cgpa" : 9.6,
              "marks" : {
                  "PHY" : 98,
                  "CHEM" : 87,
                  "MATHS" : 90
                }
    }
print(student.items()) #dict_items([('name', 'neha'), ('cgpa', 9.6), ('marks', {'PHY': 98, 'CHEM': 87, 'MATHS': 90})])

#4)dic_name.get("key") - returns the key according to the values.
student = { "name" : "neha",
              "cgpa" : 9.6,
              "marks" : {
                  "PHY" : 98,
                  "CHEM" : 87,
                  "MATHS" : 90
                }
    }
print(student.get("marks")) #{'PHY': 98, 'CHEM': 87, 'MATHS': 90}
#senario
print(student["marks2"]) #give error and stop execution of "AFTER" codes.
print(student.get("marks2")) #print non and execute "AFTER" codes. 

#5)dic_name.update(newDict) - inserts the specufied items to the dictionary.
student = { "name" : "neha",
              "cgpa" : 9.6,
              "marks" : {
                  "PHY" : 98,
                  "CHEM" : 87,
                  "MATHS" : 90
                }
    }
student.update({"city" : "delhi"})
print(student) #{'name': 'neha', 'cgpa': 9.6, 'marks': {'PHY': 98, 'CHEM': 87, 'MATHS': 90}, 'city': 'delhi'}
print(list(student))

