'''16. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', ' Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}'''
str1 = input('Enter a string: ')
str2 = input('Enter a string: ')
def insert_sting_middle(str1, str2):
    a = len(str1)//2
    b = len(str1)%2
    if b == 0:
        return str1[:a]+str2+str1[a:]
    else:
        return str1[:a]+str2+str1[a+1:]
print( insert_sting_middle(str1, str2))
