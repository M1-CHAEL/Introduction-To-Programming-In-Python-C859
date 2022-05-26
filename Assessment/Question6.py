""" Write a program with total change amount in pennies as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0

the output is:

No change

Ex: If the input is:

45

the output is:

1 Quarter
2 Dimes 

 """
total_change = int(input())

quarters = total_change//25
total_change = total_change - (quarters*25)
if quarters == 1:
    print('1 Quarter')
if quarters > 1:
    print('{} Quarters'.format(quarters))
dimes = total_change//10
total_change = total_change - (dimes*10)
if dimes == 1:
    print('1 Dime')
if dimes > 1:
    print('{} Dimes'.format(dimes))
nickels = total_change//5
total_change = total_change - (nickels*5)
if nickels == 1:
    print('1 Nickel')
if nickels > 1:
    print('{} Nickels'.format(nickels))
if total_change == 1:
    print('1 Penny')
if total_change > 1:
    print('{} Pennies'.format(total_change))