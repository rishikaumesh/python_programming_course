#! /usr/bin/python3
import os

def uselss_function(value1=2, value2=1):
    answer=value1-value2*value2
    return answer 

print(os.getpid())
print("this is from file functions_no_name_is_main.py")
print(uselss_function(4,5))
print(uselss_function())
print("This is from file functions_no_name_is_main.py")

