'''
Required knowledge: print, input, string, int,
                    int casting, variables, math operators,
                    if-elif-else, maps, functions
'''

print ('This program uses the desired operator on two numbers and shows the results')
x = int(input ('Enter the first number: '))
y = int(input ('Enter the second number: '))
op = input('Enter the operator: ')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

if op in operators:
    fn = operators[op]
    print ('{} {} {} = {}'.format(x, op, y, fn(x, y)))
else:
    print ('Oops, seems like {} is not a valid operator'.format(op))