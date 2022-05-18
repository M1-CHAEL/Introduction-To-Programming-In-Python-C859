''' Write a program that first gets a list of integers from input. That list is followed by two more integers representing lower and upper bounds of a range. Your program should output all integers from the list that are within that range (inclusive of the bounds).

Ex: If the input is:

25 51 0 200 33
0 50

the output is:

25 0 33 

The bounds are 0-50, so 51 and 200 are out of range and thus not output.

For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.
 '''
raw_values = input()
split_values = raw_values.split()
values_list = list(map(int, split_values))
raw_down_up = input()
split_down_up = raw_down_up.split()
range_list = list(map(int, split_down_up))
for i in values_list:
    if i >= range_list[0] and i <= range_list[1]:
        print(i, end=' ')