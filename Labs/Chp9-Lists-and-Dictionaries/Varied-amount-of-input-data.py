''' Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.

Ex: If the input is:

15 20 0 5

the output is:

10 20

Note: For output, round the average to the nearest integer.
 '''
input_values = input()
input_list = input_values.split()
input_list_int = list(map(int, input_list))
sum_value = sum(input_list_int)
average_value = int(sum_value/len(input_list_int))
max_value = max(input_list_int)

print('{:d} {:d}'.format(average_value, max_value))