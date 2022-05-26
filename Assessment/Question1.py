""" Given four values representing counts of quarters, dimes, nickels and pennies, output the total amount as dollars and cents.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'Amount: ${dollars:.2f}')

Ex: If the input is:

4
3
2
1

where 4 is the number of quarters, 3 is the number of dimes, 2 is the number of nickels, and 1 is the number of pennies, the output is:

Amount: $1.41

For simplicity, assume input is non-negative.
 """

quarters = float(input())
dimes = float(input())
nickels = float(input())
pennies = float(input())
total = ((quarters*25)+(dimes*10)+(nickels*10)+pennies)/100
print(f'Amount: ${total:.2f}')