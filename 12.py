#12. Write a Python program to count the occurrences of each word in a given sentence.
str1 = input("Enter a sentence: ")
s = str1.split()
result = {}
for word in s:
    result[word] = s.count(word)
print(result)