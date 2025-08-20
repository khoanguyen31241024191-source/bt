#10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.
str1 = input('enter string:')
for i in range (len(str1)):
    result = str1[i]+str1[1:i]+str1[0]
print(result)