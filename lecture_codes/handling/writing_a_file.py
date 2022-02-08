#! /usr/bin/python3

filename="our_first_text_file.txt"

file_handler=open(filename, 'w')

file_handler.write("Hello world, to the file from python!")
file_handler.close()

file_handler=open(filename,'w')

file_handler.write("this will be the next line in our file")
file_handler.close()

#a to append to file
file_handler=open(filename, 'a')
file_handler.write("This will append to the file,Hello world, to the file from python!")
file_handler.write("\n this will start a new line")
print(file_handler.closed)#this will be false because file is open
file_handler.close()

print(file_handler.closed)#this will be true because file is closed

#so we can check if file is open,if not open it 
if file_handler.closed == True:
    file_handler= open(filename,'a')

#here we read the file we just made
file_reader=open(filename, 'r')
print(file_reader)
line_from_file=file_reader.readline()#this read 1 line
print(line_from_file)

file_content=file_reader.read()#this will read the test of the file 
print(file_content)
file_handler.close()

#we opened freshed file,this will read the whole file 
file_reader=open(filename, 'r')
file_content=file_reader.read()
print(file_content)

#other ways to write to file 
open(filename, 'a').write("this write was one liner")
print(file_handler.closed)

#recommended way to handle files in python
with open(filename) as file:
    print(file.closed) #this is checking is the file is closed
    content_of_the_file=file.read()
    print(file.closed)


print(file.closed)
print(content_of_the_file)

#read line by line, using with 
with open(filename) as file2:
    for line in file2:
        print(line,end="")#this will prevent printing gaps when printing a new line
        print(f"{line}",end="")#another way as well 
        




