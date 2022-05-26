""" Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3

the output is:

3

 """
a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)
    