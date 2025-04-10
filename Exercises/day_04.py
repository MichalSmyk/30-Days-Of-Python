#1
words = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(words))
#2
words_two = ['Coding', 'For' , 'All' ]
print(' '.join(words_two))
#3
company = 'Coding For All'
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[0:6])
#10
print(company.find('Coding')) #  returns 0
#11
print(company.replace('Coding', 'Python'))
#12
for_all = 'Python For Everyone'
print(for_all.replace('Everyone', 'All'))
#13
print(company.split(' '))
#14
print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(','))
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#18
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
sentence = 'Python For Everyone'
print(''.join([word[0] for word in sentence.split(' ')]))
#19
print(''.join([word[0] for word in company.split(' ')]))
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
print(company.rfind('l'))
#23
print("You cannot end a sentence with because because because is a conjunction".index('because'))
#24
print("You cannot end a sentence with because because because is a conjunction".rindex('because'))
#25 #27
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[sentence.index('because'):sentence.rindex('because') + len('because')])
#26
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index('because'))
#28
print(company.startswith('Coding'))
#29
print(company.endswith('coding'))
#30
too_much_space = '    Coding For All      '
print(too_much_space.strip('    '))
#31
print('30DaysOfPython'.isidentifier()) # false
print('thirty_days_of_python'.isidentifier()) #true
#32
