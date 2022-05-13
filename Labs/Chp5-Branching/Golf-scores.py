''' Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies from hole to hole and is called par (i.e. 3, 4, or 5). Each score's name is based on the actual strokes taken compared to par:

    "Eagle": number of strokes is two less than par
    "Birdie": number of strokes is one less than par
    "Par": number of strokes equals par
    "Bogey": number of strokes is one more than par

Given two integers that represent par and the number of strokes used, write a program that prints the appropriate score name. Print "Error" if par is not 3, 4, or 5.

Ex: If the input is:

4
3

the output is:

Birdie
 '''

par = int(input())
strokes = int(input())

if par != 3 and par != 4 and par != 5:
    print('Error')
elif par - strokes == 2:
    print('Eagle')
elif par - strokes == 1:
    print('Birdie')
elif par == strokes:
    print('Par')
elif strokes - par == 1:
    print('Bogey')
else:
    print('Error')