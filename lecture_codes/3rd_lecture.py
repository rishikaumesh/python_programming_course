#This is a global variable 
x = 4
print(x)

def for_testing(x):
    x=3
    print(x)
for_testing(x)

print(x)

#normal way to go from local to global, from function is to use return 
def for_testing2(x):
    x=3
    print(x)
    return x
x= for_testing2(x)
print(x)

print(type(x))
print(type(5))

a=8
b=4
c=a/b
print(c)
print(type(c))

#changing type 
d=int(c)
print(d)
print(type(d))

e= 10
f=3

g=e/f
print(g)
print(int(g)) #rounding up will leave all the numbers after thd decimal point 

h=e//f
print(h)
print(type(h))

#printing remainder
i=e%f
print(i)
print(type(i))

#number is 1d line 
#4 -4,-3,-2,-1,0,1,2,3,4

#complex number is 2d number, so it is just point in plane 

k=4+4j
print(type(k))
#print(int(k)) Error 

l =k.real #printing the real number
print(l)
print(type(l)) 

p=f"with f strings we can have text and variable in the same line {l} {a} "
n="with f strings we can have text and variable in the same line"+ str(l)+" " +str(a)
print(p)
print(n)

v=[1,2,3]
print(v)
print(v[0])
print(v[2])
v.append(4)
print(v)

v[0]="we can mix text and numbers in the same list"
print(v)

#mutable vs inmutable

#for example int is immutable
x=1001
print(id(x))

x=1002
print(id(x)) #it gives the memory address 

y=x
print(id(y))
print(id(x))

# python listis mutable
q=[1,2,3]
print(id(q))

q[0]=4
print(q)
print(id(q)) # still will have the same memory address
q[2]="This still doesnt change the memory location"
print(q)
print(id(q))

w=q
print(w)
print(id(w))
w[2]=1000

print(q)
print(id(q))

def list_f(list_to_f):
    list_to_f[0]="change from function"
list_f(q)
print(q)
print(id(q))

print(q)
print(id(q))

def list_f(q):
    q[0]="function"
list_f(q)
print(w)
print(id(w))

#This does not work, list stays in local
#def list_f2():
    #local_list=[1,2,3,4]
#list_f2

####################
import copy 
e=copy.copy(w)
print(w)
print(id(w))
print(e)
print(id(e))
e[0]="finally, a fresh copy of the list"
print(f"this is w {w}")
print(id(w))
print(f"this is e{e}")
print(id(e))

list1=[1,2,3]
print(id(list1))
list2=list1[:]
print(id(list2))
list2[0]="first"
print(list1)


##tuple, like a imutable
our_first_tuple = (1,2,3,4,5)
print(type(our_first_tuple))
print(our_first_tuple[0])
print(id(our_first_tuple))













