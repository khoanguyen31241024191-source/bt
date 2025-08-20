'''14. Write a Python program that accepts a comma-separated sequence of words as input and
prints the distinct words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red'''
seq = input('Enter sequence of words: ')
a = seq.split(' ')
k = set(a)
result = sorted(k)
print(result)
