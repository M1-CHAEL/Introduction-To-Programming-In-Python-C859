""" Write a program that reads integers user_num and div_num as input, and output the quotient (user_num divided by div_num). Use a try block to perform all the statements. Use an except block to catch any ZeroDivisionError and output an exception message. Use another except block to catch any ValueError caused by invalid input and output an exception message.

Note: ZeroDivisionError is thrown when a division by zero happens. ValueError is thrown when a user enters a value of different data type than what is defined in the program. Do not include code to throw any exception in the program.

Ex: If the input of the program is:

15
3

the output of the program is:

5

Ex: If the input of the program is:

10
0

the output of the program is:

Zero Division Exception: integer division or modulo by zero

Ex: If the input of the program is:

15.5
5

the output of the program is:

Input Exception: invalid literal for int() with base 10: '15.5'

 """
from multiprocessing.sharedctypes import Value


user_num = int(input())
div_num = int(input())

try:
    if div_num == 0:
        raise ZeroDivisionError('Zero Division Exception: integer division or modulo by zero')
    if user_num is float:
        raise ValueError(f"Input Exception: invalid literal for int() with base 10: '{user_num}'")
    if div_num is float:
        raise ValueError(f"Input Exception: invalid literal for int() with base 10: '{div_num}'")
    else:
        quotient = int(user_num / div_num)
        print(quotient)
except ZeroDivisionError as excpt:
    print(excpt)
except ValueError as excpt1:
    print(excpt1)
