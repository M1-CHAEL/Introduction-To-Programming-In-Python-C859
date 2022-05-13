''' Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90.

Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

Ex: If the input is:

90

the output is:

I-90 is primary, going east/west.

Ex: If the input is:

290

the output is:

I-290 is auxiliary, serving I-90, going east/west.

Ex: If the input is:

0

the output is:

0 is not a valid interstate highway number. 

Ex: If the input is:

200

the output is:

200 is not a valid interstate highway number. 

 '''
highway_number = int(input())

if (highway_number < 100 and highway_number > 0):
    print('I-{} is primary,'.format(highway_number),end=' ')
elif (highway_number > 99 and highway_number < 1000 and (highway_number % 100 != 0)):    
    print('I-{} is auxiliary, serving I-{},'.format(highway_number,(highway_number % 100)),end=' ')
else:
    print('{} is not a valid interstate highway number.'.format(highway_number))
if (highway_number % 2 == 0) and (highway_number % 100 != 0):
    print('going east/west.')
if (highway_number % 2 != 0) and (highway_number % 100 != 0):
    print('going north/south.')
