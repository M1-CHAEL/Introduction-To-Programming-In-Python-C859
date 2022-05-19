""" rite a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. Your program should output all strings from the list that are within that range (inclusive of the bounds).

Ex: If the input is:

input1.txt
ammoniated
millennium

and the contents of input1.txt are:

aspiration
classified
federation
graduation
millennium
philosophy
quadratics
transcript
wilderness
zoologists

the output is:

aspiration
classified
federation
graduation
millennium

Notes:

    There is a newline at the end of the output.
    All input files are hosted in the zyLab and file names can be directly referred to. input1.txt is available to download so that the contents of the file can be seen.
    In the tests, the first word input always comes alphabetically before the second word input.
 """
file_to_open = input()
bound1 = input()
bound2 = input()

with open(file_to_open) as file_handle:
    list1 = [line.strip() for line in file_handle]

out = [x for x in list1 if x >= bound1 and x <= bound2]

out.sort()
print('\n'.join(map(str, out)))