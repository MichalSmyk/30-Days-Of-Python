#Exercise level 2 

print(5 + 5) #addition 
print(4 - 8) #subtraction
print(2 * 3) # multiplication
print(5 / 2) # division
print(3 ** 2) # exponentiation
print(5 // 2) #flor division
print(3 % 2) #modulus

#check data types 
print(type(10)) #int
print(type(3.14)) #float
print(type(1 + 3j)) #complex
print(type('Hello, World!')) #str
print(type([1, 2, 3])) #list
print(type({'name': 'John'})) #dictionary
print(type({9.8, 3.14, 2.7})) #set
print(type((9.8, 3.14, 2.7))) #tuple

# Exercise level 3 step 2 

#Find an Euclidian distance betweenm (2,3) and (10,8)
import math 
p1 = (2,3)
p2 = (10,8)

# calculate the distance

print(math.dist(p1, p2))