#9. Write a Python program to remove the nth index character from a nonempty string.
str1 = input("Enter a string: ")
if len(str1) != 0:
    a = int(input('remove the nth index character: '))
    result = str1[:a] + str1[a+1:]
    print(result)
else:
    print('string is empty')