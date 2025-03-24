#Exercises day 03
#1
age = 29
#2
height = 1.80
#3
complex_num = 1 + 6j
#4
base = input('Enter base: ')
height = input('Enter height: ')
print(f'The area of the triangle is {0.5 * float(base) * float(height)}')
#5
side_a = input('Enter side a: ')
side_b = input('Enter side b: ')
side_c = input('Enter side c: ')
print(f'The perimeter of the triangle is {float(side_a) +float(side_b) + float(side_c)}')
#6
length = input('Enter the length of a rectangle: ')
width = input('Enter the width of a rectangle: ')
print(f'The area of the rectangle is {float(length) * float(width)}')
print(f'The perimeter of the rectangle is {2 * (float(length) + float(width))}')
#7
pi = 3.14
radius = input('Enter the radius of the circle: ')
print(f'The area of the circle is {pi * float(radius) ** 2} and the curcumference is {2 * pi * float(radius)}')
#8
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope
print(f'The x-intercept is {x_intercept}')
#9
import math 
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
print("Slope is: ", (y2 - y1) / (x2 - x1))
print("Distance is: ", math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
#10
print(slope == slope_2)
#11
x = input('Enter x: ')

def value_of_y(x):
    print(f'The value of y is {x**2 + 6 * x + 9}')

value_of_y(x)
#12


