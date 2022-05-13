''' Auto-graded programming assignments may use a Unit test to test small parts of a program. Unlike a Compare output test, which evaluates your program's output for specific input values, a Unit test evaluates individual functions to determines if each function:

    is named correctly and has the correct parameters and return type
    calculates and returns the correct value (or prints the correct output)

In Python labs, the line if __name__ == '__main__': is used to separate the main code from the functions' code so that each function can be unit tested.

This example lab uses multiple unit tests to test the kilo_to_pounds() function.

Complete a program that takes a weight in kilograms as input, converts the weight to pounds, and then outputs the weight in pounds. 1 kilogram = 2.204 pounds (lbs).

Ex: If the input is:

10

the output is:

22.040000000000003 lbs

Note: Your program must define the function
def kilo_to_pounds(kilos)

The program below has an error in the kilo_to_pounds() function.

    Try submitting the program for grading (click "Submit mode", then "Submit for grading"). Notice that the first two test cases fail, but the third test case passes. The first test case fails because the program outputs the result from the kilo_to_pounds() function, which has an error. The second test case uses a Unit test to test the kilo_to_pounds() function, which fails.

    Change the kilo_to_pounds() function to multiply the variable kilos by 2.204, instead of dividing. The return statement should be: return (kilos * 2.204); Submit again. Now the test cases should all pass.

Note: A common error is to mistype a function name with the incorrect capitalization. Function names are case sensitive, so if a lab program asks for a kilo_to_pounds() function, a kilo_To_Pounds() function that works for you in develop mode will result in a failed unit test (the unit test will not be able to find kilo_to_pounds()).
 '''
def kilo_to_pounds(kilos):
        pounds = kilos * 2.204
        return pounds


if __name__ == '__main__':
    kilos = float(input());
    
    pounds = kilo_to_pounds(kilos);
    print(pounds, "lbs");