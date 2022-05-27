""" Write a program to calculate the total price for car wash services. A base car wash is $10. A dictionary with each additional service and the corresponding cost has been provided. Two additional services can be selected. A '-' signifies an additional service was not selected. Output all selected services along with the corresponding costs and then the total price for all car wash services.

Ex: If the input is:

Tire shine
Wax

the output is:

ZyCar Wash
Base car wash -- $10
Tire shine -- $2
Wax -- $3
----
Total price: $15

Ex: If the input is:

Rain repellent
-

the output is:

ZyCar Wash
Base car wash -- $10
Rain repellent -- $2
----
Total price: $12

 """
services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

total += base_wash
if service_choice1 in services:
    total += services[service_choice1]
if service_choice2 in services:
    total += services[service_choice2]
print('ZyCar Wash')
print('Base car wash -- $10')
if service_choice1 in services:
    print(f'{service_choice1} -- ${services[service_choice1]}')
if service_choice2 in services:
    print(f'{service_choice2} -- ${services[service_choice2]}')
print('----')
print(f'Total price: ${total}')