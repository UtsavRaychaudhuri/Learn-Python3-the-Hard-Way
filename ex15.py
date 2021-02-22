# imprting argv from the sys package 
from sys import argv
# unpacking argv 
script, filename=argv
# opening the file 
txt=open(filename)
# printing out the filename 
print(f"Here's your file {filename}:")
# printing out the contents of the file 
print(txt.read())
# asking the user for the filename input again 
print("Type the filename again:")
# the input prompt 
file_again=input("> ")
# user prompt asking for the text 
txt_again = input("> ")
# assigning the text_again variable to opening the file 
txt_again=open(file_again)
# printing the contents of text again 
print(txt_again.read())
