#! /usr/bin/python3

#binary means that it contains 2 values:
#0,1

#print number in binary form 
print(bin(11))

for i in range (0,20):
    print(f"number {i}={bin(i)}")

import numpy as np

x=np.array([1,],dtype=np.unit8)

x[0]=1
print(x[0])
x[0]=14
print(x[0])
x[0]=400
print(x[0])
print(bin(400))
print(bin(144))

y=np.array([1,],dtype=np.unit8)

y[0]=128
print(y[0])
print(bin(400))
print(bin(144))

z=np.array([1,],dtype=np.unit16)
z[0]=1
print(z[0])
z[0]=14
print(z[0])
z[0]=400
print(z[0])
print(bin(400))
print(bin(144))








