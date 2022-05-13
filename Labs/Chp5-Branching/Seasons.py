''' Write a program that takes a date as input and outputs the date's season. The input is a string to represent the month and an int to represent the day.

Ex: If the input is:

April
11

the output is:

Spring

In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:

Blue
65

the output is:

Invalid 

The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
 '''
 
input_month = input()
input_day = int(input())

if input_day > 31 or input_day <1:
    print('Invalid')
elif ((input_month == 'March' and input_day >= 20) or input_month == 'April' or input_month == 'May' or (input_month == 'June' and input_day <= 20)):
    print('Spring')
elif ((input_month == 'June' and input_day >= 21) or input_month == 'July' or input_month == 'August' or (input_month == 'September' and input_day <= 21)):
    print('Summer')
elif ((input_month == 'September' and input_day >= 22 and input_day < 31) or input_month == 'October' or input_month == 'November' or (input_month == 'December' and  input_day <= 20)):
    print('Autumn')
elif ((input_month == 'December' and input_day <= 21) or input_month == 'January' or input_month == 'February' or (input_month == 'March' and input_day <= 19)):
    print('Winter')
else:
    print('Invalid')