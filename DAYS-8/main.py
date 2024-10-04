#  FUNCTION:

def greet():
    print('Hello')
    print('ravi')

# greet()    


#  FUNCTION WITH INPUT: PASSING parameter:

#  in this examples name is parameter and ravi is argument.

def greet_with_name(name):
    print(f'Hello {name}')

# greet_with_name('ravi')


#  positional argumnet vs keyword argument 


# postitonal argument ( ORDER MATTER)
def greet(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

greet('ravi', 'norve') 


#  keyword argument(ORDER DOES NOT MATTER)

def greet(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}')

greet(location='norve', name='ravi') 