""" The Fibonacci sequence begins with 0 and 1, with all subsequent terms formed as the sum of the previous two values. For example, the first terms of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13…

Complete the fibonacci() method, which has an index, n, as parameter and returns the nth term in the sequence. Any negative index values should return -1.
fibonacci(0) 	fibonacci(1) 	fibonacci(2) 	fibonacci(3) 	fibonacci(4) 	fibonacci(5) 	fibonacci(6) 	fibonacci(7) 	fibonacci(n)
0 	1 	1 	2 	3 	5 	8 	13 	?

Ex: If the input is:

7

the output is:

fibonacci(7) is 13

Note: Use a for loop and DO NOT use recursion.
 """
def fibonacci(n):
    a = 0
    b = 1
     
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b
    


if __name__ == '__main__':
    start_num = int(input())
    print('fibonacci({}) is {}'.format(start_num, fibonacci(start_num)))