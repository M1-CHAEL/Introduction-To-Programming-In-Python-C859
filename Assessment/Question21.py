""" Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. The file contains a list of words separated by commas. Your program should output the words and their frequencies (the number of times each word appears in the file) without any duplicates.

The contents of the input1.csv are: hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy

Ex: If the input is:

input1.csv

the output is:

hello 1
cat 2
man 2
hey 2
dog 2
boy 2
Hello 1
woman 1
Cat 1

 """
import csv
file = []
count = ''
with open("input1.csv", "r") as csv_raw:
   csv_file = csv.reader(csv_raw,delimiter=',')
   for row in csv_file:
      file += row
   
   for var in file:
      if var not in count:
         print(f'{var} {file.count(var)}')
         count += var
      