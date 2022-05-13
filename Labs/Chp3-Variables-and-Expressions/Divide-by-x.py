''' Write a program using integers user_num and x as input, and output user_num divided by x three times.

Ex: If the input is:

2000
2

Then the output is:

1000 500 250
 '''
user_num = int(input())
x = int(input())
user_num //= x
print(user_num, end=" ")
user_num //= x
print(user_num, end=" ")
user_num //= x
print(user_num)