'''
Understanding super() and __init__()

Parent - Child Class relations

'''
class Hello:

   def __init__(self, name, age):
    self.name = name
    self.age = age
    print(f'{self.name} is {self.age}')
  

class Hi(Hello):
    def __init__(self, name, age, country, job):
        super().__init__(name,age)
        self.country = country
        self.job = job

        print(f'{self.name} lives in {self.country}, is {self.age} years and works as a {self.job}')


if __name__ == "__main__":

    language = Hi('Bob', 35, 'USA', 'Software Engineer')
    print(language)
    #print(intro)


'''
A Palindrome Checker
'''
import re 

string = input("Enter a word or a phrase: ")
new_string = re.sub(r'\W+', '', string.lower())

reversed_string = new_string[::-1]

if new_string == reversed_string:
    print(f"{new_string} is a palindrome")
else:
    print(f"{new_string} is not a palindrome")



'''

A Fibonacci Sequence Generator

'''

def fib(num):
        fib_sequence = {}

        for i in range(1, num + 1):
            if i <= 2:
                fib_sequence[i] = 1
            else:
                fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]

        return fib_sequence


if __name__ == "__main__":
    
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    
    fib1 = fib(n)
    print(fib1)


        

