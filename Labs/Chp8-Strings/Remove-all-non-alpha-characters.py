''' Write a program that removes all non-alpha characters from the given input.

Ex: If the input is:

-Hello, 1 world$!

the output is:

Helloworld

 '''
string = input()

s = ''.join(c for c in string if c.isalnum())
result = ''.join([i for i in s if not i.isdigit()])
print(result)