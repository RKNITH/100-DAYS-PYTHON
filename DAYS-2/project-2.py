# TIP CALCULATOR

print('Welcome to tip calculator')

bill =float(input('enter total bill '))
tip =float(input('how much tip would you like to give '))
numberOfPeople =int(input('enter number of people '))

total = bill + bill * tip/100

bill_per_person =total/numberOfPeople

print(f'Each person should pay: {bill_per_person}')
