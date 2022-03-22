# /usr/bin/python3
from itertools import zip_longest #to extend the list 

# we can zip to make tuples from list etc,...

list1=[1,2,3,4]
list2=["yksi","kaksi","kolme","nelja"]

list_combined=zip(list1,list2)
print(list_combined) #zip object

print("------")

#interating over zip object 
for zipped in list_combined:
    print(zipped)

print(list(zip(list1,list2))) #making a list 

#print(list(list_combined)) this does not work 

for i in zip(range(4),list2):
    print(i) #printing couples from 0
    print('------')

dict_to_zip={1:"1",2:"2",3:"3"}
#for key, value in dict_to_zip.items():
#    print(zip(key,value))

for i in zip_longest(range(8),list2):
    print(i)  #to extend the list and place the extra values to "none"
