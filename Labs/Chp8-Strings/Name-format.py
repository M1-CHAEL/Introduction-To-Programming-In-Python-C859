''' Many documents use a specific format for a person's name. Write a program whose input is:

firstName middleName lastName

and whose output is:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe

the output is:

Doe, P.S.

If the input has the form:

firstName lastName

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark

the output is:

Clark, J.

 '''
name_string = input()
name_split = name_string.split()
last_name = name_split[-1]
first_name = name_split[0]
first_initial = first_name[0] +'.'
second_initial = ''
if len(name_split) == 3:
    middle_name = name_split[1]
    second_initial = middle_name[0] + '.'
initials = first_initial + second_initial
print('{}, {}'.format(last_name, initials))