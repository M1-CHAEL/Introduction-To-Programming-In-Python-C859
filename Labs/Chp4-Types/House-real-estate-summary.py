
''' 
Sites like Zillow get input about house prices from a database and provide nice summaries for readers. Write a program with two inputs, current price and last month's price (both integers). Then, output a summary listing the price, the change since last month, and the estimated monthly mortgage computed as (current_price * 0.051) / 12.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f}'.format(your_value))

Ex: If the input is:

200000 
210000

the output is:

This house is $200000. The change is $-10000 since last month.
The estimated monthly mortgage is $850.00.
 '''
current_price = int(input())
last_months_price = int(input())

change = current_price - last_months_price
mortgage = (current_price * 0.051) / 12
print('This house is ${}. The change is ${} since last month.\nThe estimated monthly mortgage is ${:.2f}.'.format(current_price,change,mortgage))