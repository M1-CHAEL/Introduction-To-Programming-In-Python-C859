""" A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.

Ex: If the input is:

bob

the output is:

bob is a palindrome

Ex: If the input is:

bobby

the output is:

bobby is not a palindrome

 """

input_string = str(input())
reverse_string = input_string[::-1]

if input_string == reverse_string:
    print('{} is a palindrome'.format(input_string))
if input_string != reverse_string:
    print('{} is not a palindrome'.format(input_string))