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
print(len('python') != len('dargon'))
#13
print(f'on is found in both python and dragon {("on" in "python") and ("on" in "dragon")}')
#14
print(f'I hope this course is not full of jargon {("jargon" in "I hope this course is not full of jargon")}')
#15
print('on'not in 'python' and 'on' not in 'dragon')
#16
word_length = len('python')
float_word_length = float(word_length)
string_word_length = str(word_length)
#17
#check if number is even or not 
even_or_not = input("Enter a number: ")

def check_even_or_not(even_or_not):
    if int(even_or_not) % 2 == 0:
        print(f'{even_or_not} is an even number')
    else:
        print(f'{even_or_not} is not an even number')

check_even_or_not(even_or_not)
#18
print(7 // 3 == int(2.7))
#19
print(type('10') == type(10))
#20
print(int('9.8') == 10)
#21
hours = input('Enter hours: ')
pay_rate = input('Enter pay rate: ')
print(f'Your weekly earning is {hours * pay_rate}')
#22
years = input('Enter number of yeard you have lived: ')
seconds_in_year = 60 * 60 * 24 * 365
print(f'You have lived for {years * seconds_in_year} seconds')
#23
def display_table():
    print("1 1 1 1 1")
    for i in range(2,6):
        print(f"{i} 1 {i} {i ** 2} {1 ** 3}")

display_table()