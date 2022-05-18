""" A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc. Write a program that first takes in word pairs that consist of a name and a phone number (both strings). That list is followed by a name, and your program should output the phone number associated with that name.

Ex: If the input is:

Joe 123-5432 Linda 983-4123 Frank 867-5309
Frank

the output is:

867-5309

 """
user_input = input()
split_input = user_input.split()

names = split_input[0::2]
number = split_input[1::2]
contacts = dict(zip(names, number))

name_input = input()
print(contacts[name_input])
