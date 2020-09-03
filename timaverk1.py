n_str = input('Input n: ')
n_int = int(n_str)

print(n_int*n_int)



m_str = input('Input m: ')  # do not change this line
m_float = float(m_str)# change m_str to a float
c = 300000000**2 # remember you need c
e = m_float * c # e = 
print("e =", e)  # do not change this line



n_str = input('Input n: ')
n_int = int(n_str)
result = n_int * 2 + n_int * 3
print(result)



import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

x1_int = int(x1_str)
y1_int = int(y1_str)
x2_int = int(x2_str)
y2_int = int(y2_str)
# convert strings to ints
d = math.sqrt((x1_int - x2_int)**2 + (y1_int - y2_int)**2)
#  d =
print("d =",d)  # do not change this line



weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line

weight_float = float(weight_str)
height_float = float(height_str)

bmi = (weight_float / (height_float/100)**2)

print("BMI is: ", bmi) # do not change this line



n_str = input("Input n: ")
n_int = int(n_str)# remember to convert to an int
first_three = int(n_int / 100)# first_three =
last_two = n_int % 100# last_two =
print("first_three:", first_three)
print("last_two:", last_two)