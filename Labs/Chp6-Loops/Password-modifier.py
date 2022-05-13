''' 

Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

    i becomes 1
    a becomes @
    m becomes M
    B becomes 8
    s becomes $

Ex: If the input is:

mypassword

the output is:

Myp@$$word!
 '''
word = input()
password = ''

for char in word:
    if char == 'i':
        password += '1'
    elif char == 'a':
        password += '@'
    elif char == 'm':
        password += 'M'
    elif char == 'B':
        password += '8'
    elif char == 's':
        password += '$'
    else:
        password += char
password += '!'
print(password)