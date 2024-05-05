'''
Haris Khan

Area of a circle 

'''
import math
radius = int(input("Enter the radius:"))
area = math.pi * pow(radius, radius)
print("Area of circle: ", area)

'''
Frequency of a word in a string

'''
string = input("Enter a string of words: ")

str_ = string.split(' ') #list of stringed words
words = {}

try:
    for i in str_:
       if i in words:
        words[i] += 1
       else:
        words[i] = 1
except ValueError as e:
    print(e)

for w, i in words.items():
    print(f'Frequent Word: {w}, Count: {i}')


'''

Temperature Converter from Celsius to Fahrenheit 

'''

def temp_choice():

    unit = input("Choose which unit of temp conversion:")
    tmp = int(input("Temp: "))
    if unit == "Celsius" or unit == "C":
       print("Converting from Fahrenheit to Celsius")
       form = (tmp * 9/5) + 32 
    else:   
       print("Converting to Fahrenheit from Celsius")
       form =  ((tmp) - 32) * 5/9

    return form

if __name__ == "__main__":
   print(temp_choice())



