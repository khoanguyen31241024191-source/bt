'''3. Write a  Python program to get a string made of the first 2 and last 2 characters of a given
string. If the string length is less than 2, return the empty string instead.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String'''
a = str(input('string is: '))
if len(a)>=2:
    b = a[0]+a[1]+a[-2]+a[-1]
    print(b)
else:
    print('Empty String')