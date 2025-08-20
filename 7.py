'''7. Write a  Python program to find the first appearance of the substrings 'not' and 'poor' in a given
string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!' '''
a = str(input('Enter the string: '))
b = 'not'
c = 'poor'
pos1 = a.find(b)
pos2 = a.find(c)
if (pos1 < pos2) and pos1 !=-1 and pos2 !=-1:
    result = a[:pos1] + 'good' + a[pos2+4:]
    print(result)
else:
    print(a)