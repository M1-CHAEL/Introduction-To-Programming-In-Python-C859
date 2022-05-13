''' 

Forms often allow a user to enter an integer. Write a program that takes in a string representing an integer as input, and outputs yes if every character is a digit 0-9.

Ex: If the input is:

1995

the output is:

yes

Ex: If the input is:

42,000

or any string with a non-integer character, the output is:

no

 '''
user_string = input()

if user_string.isdigit() == True:
    print('yes')
else:
    print('no')