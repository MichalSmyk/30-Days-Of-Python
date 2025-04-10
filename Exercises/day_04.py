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