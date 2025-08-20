'''6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly' '''
a = str(input('Enter a string: '))
if len(a)>=3 and a[-3:] != 'ing':
    a += 'ing'
    print(a)
elif len(a) >3 and a[-3:] == 'ing':
    a += 'ly'
    print(a)
else:
    print('unchanged')