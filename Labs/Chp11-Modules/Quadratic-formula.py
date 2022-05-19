""" Implement the quadratic_formula() function. The function takes 3 arguments, a, b, and c, and computes the two results of the quadratic formula:

The quadratic_formula() function returns the tuple (x1, x2). Ex: When a = 1, b = -5, and c = 6, quadratic_formula() returns (3, 2).

Code provided in main.py reads a single input line containing values for a, b, and c, separated by spaces. Each input is converted to a float and passed to the quadratic_formula() function.

Ex: If the input is:

2 -3 -77

the output is:

Solutions to 2x^2 + -3x + -77 = 0
x1 = 7
x2 = -5.50
 """
# TODO: Import math module
import math

def quadratic_formula(a, b, c):
    # TODO: Compute the quadratic formula results in variables x1 and x2
    x1 = ((-b + math.sqrt(pow(b,2)-(4*a*c)))/(2*a))
    x2 = ((-b - math.sqrt(pow(b,2)-(4*a*c)))/(2*a))
    return (x1, x2)
    

def print_number(number, prefix_str):
    if float(int(number)) == number:
        print("{}{:.0f}".format(prefix_str, number))
    else:
        print("{}{:.2f}".format(prefix_str, number))
    

if __name__ == "__main__":
    input_line = input()
    split_line = input_line.split(" ")
    a = float(split_line[0])
    b = float(split_line[1])
    c = float(split_line[2])
    solution = quadratic_formula(a, b, c)
    print("Solutions to {:.0f}x^2 + {:.0f}x + {:.0f} = 0".format(a, b, c))
    print_number(solution[0], "x1 = ")
    print_number(solution[1], "x2 = ")