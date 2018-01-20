'''
Required knowledge: print, input, string, string formatting,
                    len, variables, arithmetic operators
'''

fname = input('What is your first name? ')
lname = input('What is your last name? ')

print ('Hello {} {}'.format(fname, lname))
print ('The first character of your first name is {}!'.format(fname[0]))
print ('The first character of your last name is {}!'.format(lname[0]))
print ('{} has {} characters'.format(fname, len(fname)))
print ('{} has {} characters'.format(lname, len(lname)))
print ('Your full name has {} characters'.format(len(fname) + len(lname)))