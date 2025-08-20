'''8. Write a Python function that takes a list of words and return the longest word and the length
of the longest one.
Sample Output:
Longest word: Exercises
Length of the longest word: 9'''
s = input('enter the string: ')

arr = s.split()
max_length = 0
for word in arr:
   max_length = max(max_length, len(word))

print(word, max_length)