#! /usr/bin/python3

first_dict={"name":"johan","age":24,"is a live":True}
print(first_dict)

#in list we can print the elements like this
list_example=[1,2,3]
print(list_example[2])

#This will show error as there is no index position in dictionaries
#print(first_dict[2])

#Solution
print(first_dict["age"]) #this will print 24

#add value to a dictionary
first_dict["height"]=175
print(first_dict)
print(type(first_dict))

#updating value
first_dict["height"]=173
print(first_dict)

#another way to update values:
first_dict.update({"name":"Rishika"})
print(first_dict)

def dict_to_list(list_in):
    dict_to_return={}
    for i in range(len(list_in)):
        dict_to_return[str(i)]=list_in[i]
        #print(dict_to_return)
        #print(i)
        #print(list_in[i])
    return dict_to_return

print(dict_to_list(list_example))

#dictionaries can be nested, just like tuples and lists

person1={"name":"johan","age":24,"is a live":True}
person2={"name":"jony","age":29,"is a live":True}
person3={"name":"egor","age":22,"is a live":False}

human={
    "person1":person1,
    "person2":person2,
    "person3":person3
}
print(human)
print(human["person1"]) #printing out specific list 

# person1 and human["person1"] has the same memory address
person1["name"]="juhan"
print(human)
print(id(person1))
print(id(human["person1"]))

#if we want same copy but diff memory address
human2={
    "person1":person1.copy(),
    "person2":person2.copy(),
    "person3":person3.copy()
}

print(id(person1))
print(id(human["person1"]))
print(id(human2["person1"]))

#its nested so this would not work
#It is a shallow copy, so person1 still has same memory address
human3=human.copy()
import copy 

human4=copy.deepcopy(human)
print(id(person1))
print(id(human["person1"]))
print(id(human2["person1"]))
print(id(human3["person1"]))
print(id(human4["person1"]))














