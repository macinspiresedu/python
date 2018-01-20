'''
Required knowledge: print, input, string, string, formatting, int,
                    int casting, variables, arithmetic operators
'''

print ('This program adds, subtracts, multiplies, and divides two numbers and shows the results')
x = int(input ('Enter the first number: '))
y = int(input ('Enter the second number: '))

print ('{} + {} = {}'.format(x, y, x + y))
print ('{} - {} = {}'.format(x, y, x - y))
print ('{} * {} = {}'.format(x, y, x * y))
print ('{} / {} = {}'.format(x, y, x / y))