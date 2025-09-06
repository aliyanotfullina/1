from math import*
x = float(input("Enter a number:"))
y = float(input("Enter another number:"))
z1 = (cos(x) ** 4) + (sin(y) ** 2) + (0.25 * (sin(2*x)) ** 2 - 1)
z2 = (sin(y + x)) * (sin(y - x))
z1 = round(z1,3)
z2 = round(z2,3)
print('z1 = ' , z1)
print('z2 = ' , z1)
