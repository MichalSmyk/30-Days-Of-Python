#1
empty_list = []
#2
more_than_five = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
#3
print(len(more_than_five))
#4
print(more_than_five[0]) # first
print(more_than_five[4:5]) #middle-ish
print(more_than_five[-1]) # last
#5
mixed_data_types = ['Michal', 29, 180, 'married', 'Brighton']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
middle_index = len(it_companies) // 2
print(it_companies[0])
print(it_companies[middle_index])
print(it_companies[-1])
#10
it_companies[0] = 'Meta'
print(it_companies)
#11
last_company = len(it_companies)
it_companies.insert(last_company, 'Twitter')
print(it_companies)
#12
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'ABC')
print(it_companies)

