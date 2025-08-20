''' 5. Write a  Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' '''
a = str(input('string 1: '))
b = str(input('string 2: '))
k = b[:2]+a[2:]
p = a[:2] + b[2:]
print( k, p, end=' ')