#! /usr/bin/python3

from typing import Counter


print("just testing")

for i in range (5):
    print("something")

counter=0
while True:
    counter = counter + 1
    print("not forever anymore!")
    if counter >15:
        break

counter2=0
while counter<10:
    print("Just some times!")
    counter2=counter2+1

while True:
    answer_from_user = input("if you want to end, type: end")
    if answer_from_user == "end":
        break
    else:
        print ("so you want to keep going!")



while True:
    print("forever")


