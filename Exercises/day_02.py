#Exercise level 1

# Day 2: 30 Days of programming
first_name = 'Michal'
last_name = 'Smyk'
full_name = 'Michal Smyk'
country = 'Poland'
city = 'Brighton'
age = 29
year = 2025
is_married = True
is_true = True
is_light_on = False
weather, season, month = 'rainy', 'wintert', 'February'


#Exercise level 2.1
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(weather))
print(type(season))
print(type(month))

#Exercise level 2.2
print(len(first_name))

#Exercise level 2.3
print(len(first_name) == len(last_name))

#Exercise level 2.4
num_one = 5
num_two = 4

#Exercise level 2.5
total = num_one + num_two

#Exercise level 2.6
diff = num_two - num_one

#Exercise level 2.7
product = num_one * num_two

#Exercise level 2.8
division = num_one / num_two

#Exercise level 2.9
reminder = num_one % num_two

#Exercise level 2.10
exp = num_one ** num_two

#Exercise level 2.11
floor_division = num_one // num_two

#Exercise level 2.12
#I
circle_radius = 30
area_of_circle = 3.14 * (circle_radius ** 2)

#II
circum_of_circle = 2 * 3.14 * circle_radius

#III
user_radius = float(input('Enter the radius of the circle: '))
area_of_circle_user = 3.14 * (user_radius ** 2)
print(f'The area of the circle with radius {user_radius} is {area_of_circle_user}')