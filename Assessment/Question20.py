""" Write a program that reads a text file containing synonyms for a word and outputs synonyms that begin with a specified letter.

Use the attached file educate.txt to help you write and test your program. This file contains synonyms for the word "educate" listed in alphabetical order, with each row containing synonyms sharing the same first letter, separated by a space. The contents of educate.txt are as follows:

brainwash brief
civilize coach cultivate
develop discipline drill
edify enlighten exercise explain
foster
improve indoctrinate inform instruct
mature
nurture
rear
school
train tutor

Your program should read input from the user in the format of a word, a line break, and a letter. The program should open a text file associated with the input word.

The program should then store the contents of the text file into a dictionary, predefined in the program. Finally the program should search the dictionary and outputs all the synonyms that begin with the input letter, one synonym per line, or a message if no synonyms that begin with the input letter are found.

Hint: Use the first letter of a synonym as the key when storing the synonym into the dictionary. Assume all letters are in lowercase.

For example, if the input of the program is:

educate
c

the program opens the file educate.txt, then produces the following output:

civilize
coach
cultivate

If the input of the program is:

educate
a

then the program outputs:

No synonyms for educate begin with a.

 """
values = []
index = []

with open("educate.txt", "r") as input_file:
      for line in input_file:
         values += [line]
      for string in values:
         index += (string[0])
sort_values = [string.split() for string in values]         
synonyms = dict(zip(index, sort_values))


input_value = input()
input_char = input()

if input_char not in synonyms:
   print(f'No synonyms for {input_value} begin with {input_char}')
if input_char in synonyms:
   for i in synonyms[input_char]:
      print(i)