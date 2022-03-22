#! /usr/bin/python3

def ask_number_usr():
    while True:
        try:
            ask_number_usr=int(input("Give a number as a digit,like 3: "))
            return ask_number_usr
        except ValueError:
            pass

if __name__ == "__main__":
    ask_number_usr()

