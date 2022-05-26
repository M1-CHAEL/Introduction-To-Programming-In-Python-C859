""" Mad Libs are activities that have a person provide various words, which are then used to complete a short story in unexpected (and hopefully funny) ways.

Complete the program to read the needed values from input, that the existing output statement(s) can use to output a short story.

Ex: If the input is:

Eric
Chipotle
12
cars

Then the output is:

Eric went to Chipotle to buy 12 different types of cars

 """

first_name = str(input())
generic_location = str(input())
whole_number = str(input())
plural_noun = str(input())


print(first_name, 'went to', generic_location, 'to buy', whole_number, 'different types of', plural_noun)