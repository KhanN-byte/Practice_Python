
'''
dictionaries

translations = {"hello": "hola", "bye": "adios", "thank you": "gracias"}

print(translations["hello"])
'''


'''
try/except raise an exception

string = "whatever"
try: 
    num = int(string)
except ValueError as err:
    print("The string is not a number", err)
'''

'''
File I/O

file = open("example.txt", "w")
file.writelines("Yes I also like coding in python and java")
file.close()
content = open("example.txt", "r")
print(content.read())

'''

'''
Functions 

def sq (num):
    return num * num

def main():
    sq(x)

if __name__ == "__main__":
    print(sq(3))

'''

'''

User Input 

name = input("Whats your name:")
print(f"My name is {name}")

'''

'''
Lists

ord = [1, {"Haha": "Laughing", "Sad": "Emotional"}, 'LOL']

print(ord)
print(ord[0])
ord[1] = 5
print(ord)
'''

'''

Loops

fruits = ["apple", "banana", "oranges"]
for i in fruits:
    print(i)

i = 0 
while i < len(fruits):
    print(fruits[i])
    i += 1
    
'''


