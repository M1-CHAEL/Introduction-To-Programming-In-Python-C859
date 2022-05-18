''' Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2

the output is:

2 4 10 12 39

For coding simplicity, follow every output value by a space. Do not end with newline.
 '''
raw_values = input()
split_values = raw_values.split()
values_list_int = list(map(int, split_values))
values_list_int.sort()

for val in values_list_int:
    if val >= 0:
        print(val, end=' ')
