#! /usr/bin/python3

while True:
    try:
        answer=int(input("give a number: "))
        int_answer=int(answer)
        calc=int_answer*3
        print(calc)
        break

    except ValueError as err :
        print(f"{type(err).__name__} was raised:{err} ")
        print("you did not give a valid answer")



