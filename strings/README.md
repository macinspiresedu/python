# Strings
## String Type
Introduce the string type and describe some typical usages (usernames, passwords, etc.). Also, explain how strings can
be constructed with single or double quotes. Highlight when
to best use either. 

### Exercise
Have students print "I'm learning Python!", or any other phrase that uses an apostrophe. Then have them print a statement using double quotes like: 'He said: "I am leaving!"'.

```python3
print ("I'm learning Python :D")
print ('He said: "I am leaving!"')

```

## String Escape Characters
Explain the use of escape characters. In particular, show them the three escape characters: \', \", and \n.

### Exercise
Have students print the same string as before. But this time, they must use escape characters and add a newline.

```python3
print ('I\'m learning Python :D\n')
print ("He said: \"I am leaving!\"\n")
```

## String Concatenation
Explain how the string concatenation operator works.

### Exercise
Have students construct their full names using string
concatenation.

```python3
print ("John" + "Doe")
```

To demonstrate that any numbers of strings can be concatenated, have them concatenate more than 2 strings like:

```python3
print ("Hi" + " I" + " am" + " John" + "!")
```

## String Multiplication 
Explain how the string multiplication operator works.

### Exercise
Have students multiply a few strings.

```python3
print ("Hi!" * 5)
print ("Hey!" * 3)
```

## String Indexing
Explain how string indexing works. This is the student's first
exposure to array indexing, so explain the concept that in
most programming languages, sequences start counting from 0.
Also, speak about Python's ':' operator to take part of a string.

### Exercise
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


## String Length
Introduce students to the **len** function.

### Exercise
Have students print out the character length of their name.

```python3
print (len('John'))
print (len('Doe'))
```

Use the len function in a formatted string like so:

```python3
print ('Hi, I am {} and my name has {} characters.'.format('John', len('John')))
```