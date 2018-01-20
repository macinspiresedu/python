'''
Required knowledge: print, input, string, int,
                    int casting, variables, math operators,
                    comparison operators, if-elif-else 
'''

print ('This program uses the desired operator on two numbers and shows the results')
x = int(input ('Enter the first number: '))
y = int(input ('Enter the second number: '))
op = input('Enter the operator: ')


if op == '+':
    print ('{} + {} = {}'.format(x, y, x + y))
elif op == '-':
    print ('{} - {} = {}'.format(x, y, x - y))
elif op == '*':
    print ('{} * {} = {}'.format(x, y, x * y))
elif op == '/':
    print ('{} / {} = {}'.format(x, y, x / y))
else:
    print ('Oops, seems like {} is not a valid operator'.format(op))
