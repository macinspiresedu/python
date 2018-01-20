'''
Required knowledge: print, input, string, string formatting,
                    len, variables, comparison operators,
                    if-elif-else
'''

fname = input('What is your first name? ')
lname = input('What is your last name? ')

print ('Hello {} {}'.format(fname, lname))

if len(fname) > len(lname):
    print ('Your first name has more characters than your last name')
else:
    print ('Your last name has more characters than your first name')