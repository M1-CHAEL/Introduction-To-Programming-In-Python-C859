''' Driving is expensive. Write a program with a car's miles/gallon and gas dollars/gallon (both floats) as input, and output the gas cost for 10 miles, 50 miles, and 400 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f}'.format(your_value))

Ex: If the input is:

20.0
3.1599

the output is:

1.58
7.90
63.20

Your program must define and call the following driving_cost() function. Given input parameters driven_miles, miles_per_gallon, and dollars_per_gallon, the function returns the dollar cost to drive those miles.

Ex: If the function is called with:

50  20.0  3.1599

the function returns:

7.89975

def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon)

Your program should call the function three times to determine the gas cost for 10 miles, 50 miles, and 400 miles.
 '''
 # Define your function here.
def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    driving_cost = (driven_miles/miles_per_gallon)*dollars_per_gallon
    return driving_cost

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    print('{:.2f}'.format(driving_cost(10, miles_per_gallon, dollars_per_gallon)))
    print('{:.2f}'.format(driving_cost(50, miles_per_gallon, dollars_per_gallon)))
    print('{:.2f}'.format(driving_cost(400, miles_per_gallon, dollars_per_gallon)))
