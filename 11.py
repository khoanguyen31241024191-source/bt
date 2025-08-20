#11.Write a Python program to remove characters that have odd index values in a given string.
str1 = input("enter string:")
result = ''
for i in range (len(str1)):
    k = i%2
    if k == 0:
        result += str1[i]
    else:
        result += ''
print(result)
