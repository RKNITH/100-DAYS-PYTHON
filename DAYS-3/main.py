#  LEARNING IF-ELSE LOOP

# CHECK ODD OR EVEN

a =int(input('Enter number '))

if(a % 2 ==0):
    print('Even')
else:
    print('Odd')    






#PIZZA DELEVIRIES:
# congratulation, you have got a job at Python Pizza! You first job is to build an automatic pizza order program.
# Based on the user's order, work out their final bill. Use the input() to get the user's preferences and then add up the total for their order and tell them how much they have to pay.
# small pizza(s):15
# medium pizza(m):20
# large pizza(l):25
#  add peperoni for small pizza 2 and for other pizza 3.
# extra chees 2

print('Welcome to Python Pizza Deliveries')
size =input('What size pizza do you want S, M, L ')
pepperoni =input('do you want pepperoni on your pizza Y or N ')
extra_cheese =input('do you want extra cheese Y or N ')

total =0
if(size =='S'):
    total =15
elif size =='M':
    total =20
elif size =='L':
    total =25
if pepperoni =='Y':
    if size =='S':
        total +=2
    else:
        total +=3
if extra_cheese =='Y':
    total +=2

print(f'your total bill is {total}')                            



# LOGICAL OPERATOR

# A AND B BOTH ARE TRUE: A and B
# A OR B
