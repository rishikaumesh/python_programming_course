#! /usr/bin/python3

tuple_values=(1,2,3,4,5)
print(type(tuple_values))
print(tuple_values)

print("----------")
#example one, as many variables as values as tuples
one,two,three,four,five=tuple_values
print(type(one))
print(one)

print("----------")
#more values in tuple than variable 
#the star means put eveyrthing else in a list
a,b,c, *d=tuple_values
print(a)
print(b)
print(c)
print(d)
print(type(d))
print("----------")

#let's define a function where we dont know how many arguments there will be when called
def show_cities(*args):
    print(f"what is the type of this *args thing: {type(args)}")
    for city in args:
        print(city)

show_cities("rome","paris","pori")
print("----------")
show_cities("rome","paris","pori","london")
print("----------")
show_cities("rome")


def show_cities3(first_city,*args):
    print(f"what is the type of this *args thing: {type(args)}")
    print(f"the first city is: {first_city}")
    for city in args:
        print(city)

show_cities3("rome","paris","pori")
print("----------")
show_cities3("rome","paris","pori","london")
print("----------")
show_cities3("rome")

#############################################
#** can be used to unpack dictionaries 
dict1={1:"v1", 2:"v2", 3:"v3"}
dict2={4:"v4", 5:"v5", 6:"v6"}
## this doesnt work with dictionaries
## dict3=dict1+dict2

##combines the two dictionaries
dict3={**dict1,**dict2}
print(dict3)

#only Prints keys
dict4={*dict1,*dict2}
print(dict4)

dict5=dict1
print(dict1 is dict5)
dict6={**dict1}
print(dict1 is dict6)

print("-----------------------")
def average_house_values(**kwargs):
    print(f"the type of kwargs is:{type(kwargs)}")
    for key, value in kwargs.items():
        print(f"key:{key},value:{value}")

average_house_values(pori=1000000,
                    helsinki=7000000,
                    turku=900000)

print("------------------")
def example (first, *args, **kwargs):
        print(f"what is the type of this *args thing: {type(args)}")
        print(f"the type of kwargs is:{type(kwargs)}")
        print(f"the first is:{first}")
        for value in args:
            print(value)
        for key,value in kwargs.items():
            print(f"key:{key},value:{value}")
        
example("this is the first",
        "arg1",
        "arg2",
        kwargs1="value1",
        kwargs2="value2",
        kwargs3="value3",
    )
















