""" Write a program that reads the student information from a tab separated values (tsv) file. The program then creates a text file that records the course grades of the students. Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, and the Final score of a student. A sample of the student information is provided in StudentInfo.tsv. Assume the number of students is at least 1 and at most 20.

The program performs the following tasks:

    Read the file name of the tsv file from the user.
    Open the tsv file and read the student information.
    Compute the average exam score of each student.
    Assign a letter grade to each student based on the average exam score in the following scale:
        A: 90 =< x
        B: 80 =< x < 90
        C: 70 =< x < 80
        D: 60 =< x < 70
        F: x < 60
    Compute the average of each exam.
    Output the last names, first names, exam scores, and letter grades of the students into a text file named report.txt. Output one student per row and separate the values with a tab character.
    Output the average of each exam, with two digits after the decimal point, at the end of report.txt. Hint: Use the format specification to set the precision of the output.

Ex: If the input of the program is:

StudentInfo.tsv

and the contents of StudentInfo.tsv are:

Barrett    Edan    70  45  59
Bradshaw    Reagan  96  97  88
Charlton    Caius   73  94  80
Mayo    Tyrese  88  61  36
Stern    Brenda  90  86  45

the file report.txt should contain:

Barrett    Edan    70  45  59  F
Bradshaw    Reagan  96  97  88  A
Charlton    Caius   73  94  80  B
Mayo    Tyrese  88  61  36  D
Stern    Brenda  90  86  45  C

Averages: midterm1 83.40, midterm2 76.60, final 61.60

 """
#UNSOLVED
file_to_open = input()
i = 0
x = 0
z = 0
midterm1 = 0.0
midterm2 = 0.0
final = 0.0
output2 = ''
output_list = []
final_output = open('report.txt', 'w')

def grade(a, b, c):
    ave = (int(a)+int(b)+int(c))/3
    return ave
    
with open(file_to_open) as file_handle:
    list1 = [line.split('\t') for line in file_handle]
while x < len(list1):
    list1[x][4] = list1[x][4].strip('\n')
    x += 1
# TODO: Read a file name from the user and read the tsv file here. 
while i < len(list1):
    a = list1[i][2]
    b = list1[i][3]
    c = list1[i][4]
    if grade(a,b,c) >= 90:
        list1[i].append('A')
    elif grade(a,b,c) < 90 and grade(a,b,c) >= 80:
        list1[i].append('B')
    elif grade(a,b,c) < 80 and grade(a,b,c) >= 70:
        list1[i].append('C')
    elif grade(a,b,c) < 70 and grade(a,b,c) >= 60:
        list1[i].append('D')
    elif grade(a,b,c) < 60:
        list1[i].append('F')
    midterm1 += float(list1[i][2])
    midterm2 += float(list1[i][3])
    final += float(list1[i][4])
    i += 1
midterm1 = midterm1/len(list1)
midterm2 = midterm2/len(list1)
final = final/len(list1)

x = 0
while x < len(list1):
    list1[x][5] = list1[x][5]+'\n'
    x += 1


for z in list1:
    final_output.write(z)
final_output.write('\nAverages: midterm1 {}, midterm2 {}, final {}'.format(midterm1,midterm2,final))

final_output.close()
