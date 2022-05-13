import math

r = math.pow(2,(1/12))
f_initial = float(input())

value_1 = (f_initial * float(math.pow(r,0)))
value_2 = (f_initial * float(math.pow(r,1)))
value_3 = (f_initial * float(math.pow(r,2)))
value_4 = (f_initial * float(math.pow(r,3)))
value_5 = (f_initial * float(math.pow(r,4)))
print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'.format(value_1,value_2,value_3,value_4,value_5))