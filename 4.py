'''4. Write a  Python program to get a string from a given string where all occurrences of its first
char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t' '''
a = str(input('nhap: ' ))
k = a[0]
b = a[0]
for i in range (1, len(a)):
    if a[i] == k:
        b += '$'
    else:
        b += a[i]
print(b)