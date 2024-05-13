'''

Count occurrences of a character in a word
Python Practice
05_12.py

'''

inputstr = input('Enter a string:')
char = input('Enter the character to count:')

count = inputstr.lower().count(char.lower())
print(f'Character {char} occurs {count} times')
print(f'ASCII of Character {char} is {ord(char)}')



sentence = input('Enter a sentence:')
words = sentence.split()

max_length = 0
longestW = ""

for i in words:
    if len(i) > max_length:
        longestW = i

print(f'Longest word is {longestW}')


list_1 = input('Enter 1st list of numbers:').split()
list_2 = input('Enter 2nd list of numbers:').split()


commonlist = list(set(list_1) & set(list_2))
print(f'Common elements are:{commonlist}')

nums = [float(x) for x in input('Enter list of numbers with spaces:').split()]

ascending = sorted(nums)
descending = sorted(nums, reverse = True)
print(f'Numbers in order: {ascending}')
print(f'Numbers in reversed: {descending}')

