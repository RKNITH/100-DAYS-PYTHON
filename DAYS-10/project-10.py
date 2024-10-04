#  CALCULATOR:

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a, b):
    return a/b

operations ={
    '+': add,
    '-':subtract,
    '*':multiply,
    '/': divide
}

def calculator():
    num1 =float(input('Enter first number '))
    should_accumulate =True
    while should_accumulate:
        
        num2 =float(input('Enter second number '))
        for symbol in operations:
            print(symbol)
        operation_symbol =input('pic an openration ')
        answer = operations[operation_symbol](num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer}')

        choice =input(f' type yes to calculating with {answer} , or type no to end calculation ').lower()

        if choice =='yes':
            num1 =answer
        else:
            should_accumulate =False
            print('\n'*20)  
            calculator()  
