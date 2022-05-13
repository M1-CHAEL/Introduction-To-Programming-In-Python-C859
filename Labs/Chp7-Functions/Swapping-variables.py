''' Write a program whose input is two integers and whose output is the two integers swapped.

Ex: If the input is:

3
8

the output is:

8 3

Your program must define and call the following function. swap_values() returns the two values in swapped order.
def swap_values(user_val1, user_val2)
 '''
def swap_values(user_val1, user_val2):
    print(user_val2, end=' ')
    print(user_val1)
    temp1 = user_val2
    user_val2 = user_val1
    user_val1 = temp1
    return (user_val1, user_val2)
if __name__ == '__main__': 
    user_val1 = int(input())
    user_val2 = int(input())
    swap_values(user_val1, user_val2)