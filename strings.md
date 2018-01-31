# Strings
## String Type
Introduce the string type and describe some typical usages
(usernames, passwords, etc.). Also, explain how strings can
be constructed with single or double quotes. Highlight when
to best use either. 

### Exercise
Have students print "I'm learning Python!", or any other phrase that uses an apostrophe. 
Then have them print a statement using double quotes like: 'He said: "I am leaving!"'.

```python3
print ("I'm learning Python :D")
print ('He said: "I am leaving!"')

```

## String Escape Characters
Explain the use of escape characters.
In particular, show them the three escape characters: \', \", and \n.

### Exercise
Have students print the same string as before.
But this time, they must use escape characters and add a newline.

```python3
print ('I\'m learning Python :D\n')
print ("He said: \"I am leaving!\"\n")
```

## String Formatting
Introduce students to the basic usage of Python3's formatting functionality.

### Exercise
Have students write an introductory statement with their names being used:

```python3
print ('Hi, I am {}'.format('John'))
```

And full name to demonstrate multiple formatted values:

```python3
print ('Hi, I am {} {}'.format('John', 'Doe'))
```

## User Input
Introduce the **input** function and show how user input can be stored in
a variable.

### Exercise
Have students prompt users for their name and then respond with a greeting 
using their name.

```python3
name = input("What is your name: ")
print ('Hi {}!'.format(name))
```

Then, extend the program to ask the user for their age. Then, use the user's age
to inform them of when they will 100 years old. Explain the **int** function
if this is their first exposure to it.

```python3
name = input("What is your name: ")
age = int(input("How old are you: "))
print ('Hi {}!'.format(name))
print ('You will be 100 years old in the year {}'.format(100 - age + 2018))
```


## String Length
Introduce students to the **len** function.

### Exercise
Extend the previous exercise having the students
print the amount of character's in the user's name.

```python3
name = input("What is your name: ")
age = int(input("How old are you: "))
print ('Hi {}!'.format(name))
print ('You will be 100 years old in the year {}'.format(100 - age + 2018))
print ('You have {} characters in your name'.format(len(name)))
``` 


## String Indexing
Explain how string indexing works. This is the student's first
exposure to array indexing, so explain the concept that in
most programming languages, sequences start counting from 0.
Also, speak about Python's ':' operator to take part of a string.

### Exercise
Extend the previous exercise by having the students
print the first and last characters of the user's name.

```python3
name = input("What is your name: ")
age = int(input("How old are you: "))
print ('Hi {}!'.format(name))
print ('You will be 100 years old in the year {}'.format(100 - age + 2018))
print ('You have {} characters in your name'.format(len(name)))
print ('The first character in your name is {}'.format(name[0]))
print ('The last character in your name is {}'.format(name[-1]))
```

## String Concatenation
Explain how the string concatenation operator works.

### Exercise
Extend the previous exercise by having the students
ask the user for their last name, and then printing out
the full name using concatenation.

```python3
fname = input("What is your first name: ")
lname = input("What is your last name: ")
age = int(input("How old are you: "))
print ('Hi {}!'.format(fname + " " + lname))
print ('You will be 100 years old in the year {}'.format(100 - age + 2018))
print ('You have {} characters in your name'.format(len(fname)))
print ('The first character in your name is {}'.format(fname[0]))
print ('The last character in your name is {}'.format(fname[-1]))
```
