# MacInspires Python Curriculum

## Objective
After the completion of this course, students will have a cursory level understanding of the Python programming language. Specifically, students will leave the course with a basic understanding of types, variables, selection, lists, loops, functions and classes. If time permits, students will have built a Pong-like game using the Tkinter library.

## Materials
Students will learn core Python concepts and run exercises in the cloud environment provided by [repl.it.](https://repl.it/).

## Fundamentals

### Introduction
#### What is Python?
Introduce students to coding and Python in particular.
Explain the difference between computer code, a program, and
a programming language like Python.

#### What is repl.it?
Introduce students to the repl development environment. Show them the difference between the editor and the console and how to run their code using 'Run' button.

#### Demonstrate 'Hello World'
Use the repl example to show the Python3 'Hello World' one-liner.

#### What is the print function
Explain the usage of the print function and how it outputs a value to the console.

##### Exercise
Have students print out a few things to the console like:

```python3
print ("Hello, I'm John")
print ("I am 12 years old!")
print ("My favorite color is blue!")
print ("My favorite food is pizza!")
```

Ensure that they always enclose their strings with quotes. Further lessons will have them print out non-string values.

#### Comments
##### Exercise
Have students comment out one of their print statement. Click run so that they can see that that line of code doesn't execute.


### Calculations
#### Values and Types
Explain the distinction between values and types.

#### Integers
Introduce the integer type.

##### Exercise
Have students print out a few numbers to the console like:
```python3
print (2)
print (20000000)
print (99999999999999)
```

#### Floats
Introduce the float type.

##### Exercise
Have students print out a few numbers to the console like:
```python3
print (3.14)
print (2.71)
print (99.99)
```

#### Arithmetic Operators
Introduce the four major mathematical operators (+, -, *, /). If they haven't been taught PEMDAS yet, give them a brief explanation
of it, demonstrating that the same rules apply in Python.

##### Exercise
Have students print out a few mathematical expressions:
```python3
print (2 + 3)
print (7.3 - 2.3)
print (5 * 1)
print (100.0 / 20.0)
```

Make the expressions more complicated, using parenthesis and multiple operators.

### Strings
#### String Type
Introduce the string type and describe some typical usages (usernames, passwords, etc.). Also, explain how strings can
be constructed with single or double quotes. Highlight when
to best use either. 

##### Exercise
Have students print "I'm learning Python!", or any other phrase that uses an apostrophe. Then have them print a statement using double quotes like: 'He said: "I am leaving!"'.

```python3
print ("I'm learning Python :D")
print ('He said: "I am leaving!"')

```

#### String Escape Characters
Explain the use of escape characters. In particular, show them the three escape characters: \', \", and \n.

##### Exercise
Have students print the same string as before. But this time, they must use escape characters and add a newline.

```python3
print ('I\'m learning Python :D\n')
print ("He said: \"I am leaving!\"\n")
```

#### String Concatenation
Explain how the string concatenation operator works.

##### Exercise
Have students construct their full names using string
concatenation.

```python3
print ("John" + "Doe")
```

To demonstrate that any numbers of strings can be concatenated, have them concatenate more than 2 strings like:

```python3
print ("Hi" + " I" + " am" + " John" + "!")
```

#### String Multiplication 
Explain how the string multiplication operator works.

##### Exercise
Have students multiply a few strings.

```python3
print ("Hi!" * 5)
print ("Hey!" * 3)
```

#### String Indexing
Explain how string indexing works. This is the student's first
exposure to array indexing, so explain the concept that in
most programming languages, sequences start counting from 0.
Also, speak about Python's ':' operator to take part of a string.

##### Exercise
Have students use array indexing to access certain characters/substrings of the string 'MacInspires'.

The first character:
```python3
print ('MacInspires'[0])
```

The first 'I':
```python3
print ('MacInspires'[3])
```

The last character:
```python3
print ('MacInspires'[-1])
```

Just 'Mac'
```python3
print ('MacInspires'[0:3])
```

Just 'Inspires'
```python3
print ('MacInspires'[3:])
```


#### String Formatting
Introduce students to the basic usage of Python3's formatting functionality.

##### Exercise
Have students write an introductory statement with their names being used:

```python3
print ('Hi, I am {}'.format('John'))
```

And full name to demonstrate multiple formatted values:

```python3
print ('Hi, I am {} {}'.format('John', 'Doe'))
```


#### String Length
Introduce students to the **len** function.

##### Exercise
Have students print out the character length of their name.

```python3
print (len('John'))
print (len('Doe'))
```

Use the len function in a formatted string like so:

```python3
print ('Hi, I am {} and my name has {} characters.'.format('John', len('John')))
```

### Variables
#### Variables and Objects
Introduce variables and explain the distinction between variables
and objects. Also, explain the rules for variable construction.

##### Exercise
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

#### User Input
Introduce the **input** function and how user input can be stored in
a variable.

##### Exercise
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
