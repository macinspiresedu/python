# Variables
## Variables and Objects
Introduce variables and explain the distinction between variables
and objects. Also, explain the rules for variable construction.

### Exercise
Have students create a variable for their first and last name
and print a formatted string using both.

```python3
first = 'John'
last = 'Doe'
print ('Hi, I am {} {}'.format(first, last))
```

To demonstrate a variable's ability to be updated, have them do a simple exercise
where a variable is updated and then printed on the screen like so:

```python3
count = 3
print ('Hi' * count)
count = 2
print ('Hi' * count)
count = 1
print ('Hi' * count)
```

## User Input
Introduce the **input** function and how user input can be stored in
a variable.

### Exercise
Have students prompt users for their name and then respond with a greeting 
using their name.

```python3
name = input('What is your name? ')
print ('Hi {}. Your name has {} characters.'.format(name, len(name)))
```

Also, have the students create a program that asks the user to enter their
name and their age. Then, print out a message that tells them the year in
which they will 100 years old.

```python3
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2018 - age) + 100)
print(name + " will be 100 years old in the year " + year)
```