""" Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt. Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in the input file. Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.

Ex: If the input is:

file1.txt

and the contents of file1.txt are:

20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote

the file output_keys.txt should contain:

10: Will & Grace
12: Murder, She Wrote
14: Dallas
20: Gunsmoke; Law & Order
30: The Simpsons

and the file output_titles.txt should contain:

Dallas
Gunsmoke
Law & Order
Murder, She Wrote
The Simpsons
Will & Grace

Note: There is a newline at the end of each output file, and file1.txt is available to download.
 """
file_name = input()
user_file = open(str(file_name))
output_list = user_file.readlines()
my_dict = {}
show_list = []
show_list_split = []
for i in range(len(output_list)):
    temp_list = []
    list_object = output_list[i].strip('\n')
    if (i + 1 < len(output_list) and (i % 2 == 0)):
        if int(list_object) in my_dict:
            my_dict[int(list_object)].append(output_list[i + 1].strip('\n'))
        else:
            temp_list.append(output_list[i + 1].strip('\n'))
            my_dict[int(list_object)] = temp_list
            
my_dict_sorted_by_keys = dict(sorted(my_dict.items()))
for x in my_dict.keys():
    show_list.append(my_dict[x])
for x in show_list:
    for i in x:
        show_list_split.append(i)
show_list_split = sorted(show_list_split)
f = open('output_keys.txt', 'w')
for key, value in my_dict_sorted_by_keys.items():
    f.write(str(key) + ': ')
    for item in value[:-1]:
        f.write(item + '; ')
    else:
        f.write(value[-1])
        f.write('\n')
        
f.close()
f = open('output_titles.txt', 'w')
for item in show_list_split:
    f.write(item + '\n')
f.close()