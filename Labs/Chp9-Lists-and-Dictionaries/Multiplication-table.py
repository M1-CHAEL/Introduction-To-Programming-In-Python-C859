''' Print the two-dimensional list mult_table by row and column. On each line, each character is separated by a space. Hint: Use nested loops.

Sample output with input: '1 2 3,2 4 6,3 6 9':

1 | 2 | 3
2 | 4 | 6
3 | 6 | 9
 '''

user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]
for row_index, row in enumerate(mult_table):
    for column_index, column in enumerate(row):
        print('{}'.format(column), end='')
        if column != row[-1]:
            print(' |', end=' ')
    print()