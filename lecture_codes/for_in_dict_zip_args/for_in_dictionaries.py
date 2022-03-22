#! /usr/bin/python3

#key must be unique

some_dict = {1:"value1", 2:"value2", 3:"value3", 1:"value1"}

print(some_dict)



#for with .items()

for item in some_dict.items() :

    print(item)

    print(type(item))



for key, value in some_dict.items() :

    print(f"key: {key} type is: {type(key)}")

    print(f"value: {value} type is: {type(key)}")



#key and value are just names for variables, but they make the code more readable

for k, v in some_dict.items() :

    print(f"key: {k} type is: {type(k)}")

    print(f"value: {v} type is: {type(k)}")

print(some_dict.items())
print(type(some_dict.items()))

for key in some_dict.keys():
    print(f"key:{key} type is: {type(key)}")

keys=some_dict.keys()
print(keys)
#this doesnt work
#print(keys[0])

keys_list=list(keys)
print(type(keys_list))
print(keys_list[0])

#Here we have list of tuples from the items 
items=some_dict.items()
items_list=list(items)
print(items_list[0])
print(items_list[0][0])


for value in some_dict.items():
    print(f"value:{value} type is: {type(value)}")

values=some_dict.values()
print(values)
#this doesnt work
#print(keys[0])
values_list=list(values)
print(type(values_list))
print(values_list[0])

#we can check if dictionaries values contain some value
print("value1" in values)
#same for keys
print("1" in keys)
#it is false, because key is int, not str 
# so we need to do this :
print(1 in keys)



