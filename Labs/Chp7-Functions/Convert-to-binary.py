''' Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the integer in binary. For an integer x, the algorithm is:

As long as x is greater than 0
   Output x % 2 (remainder is either 0 or 1)
   x = x // 2

Note: The above algorithm outputs the 0's and 1's in reverse order. You will need to write a second function to reverse the string.

Ex: If the input is:

6

the output is:

110

The program must define and call the following two functions. Define a function named int_to_reverse_binary() that takes an integer as a parameter and returns a string of 1's and 0's representing the integer in binary (in reverse). Define a function named string_reverse() that takes an input string as a parameter and returns a string representing the input string in reverse.
def int_to_reverse_binary(integer_value)
def string_reverse(input_string)
 '''
def int_to_reverse_binary(integer):
    binary_output = ''
    while integer > 0:
        binary_output += str(integer % 2)
        integer = integer // 2
        if integer < 1:
            break
    return binary_output
def string_reverse(input_string):
    reverse_string = input_string[::-1]
    return reverse_string
if __name__ == '__main__':
    integer_input = int(input())
    print(string_reverse(str(int_to_reverse_binary(integer_input))))
