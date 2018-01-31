# Calculations & Variables
## Values and Types
Explain the distinction between values and types.

## Integers
Introduce the integer type.

### Exercise
Have students print out a few numbers to the console like:
```python3
print (2)
print (20000000)
print (99999999999999)
```

## Floats
Introduce the float type.

### Exercise
Have students print out a few numbers to the console like:
```python3
print (3.14)
print (2.71)
print (99.99)
```

## Arithmetic Operators
Introduce the four major mathematical operators (+, -, *, /).
If they haven't been taught PEMDAS yet, give them a brief explanation
of it, demonstrating that the same rules apply in Python.

### Exercise
Have students print out a few mathematical expressions:
```python3
print (2 + 3)
print (7.3 - 2.3)
print (5 * 1)
print (100.0 / 20.0)
```

Make the expressions more complicated, using parenthesis and multiple operators.

## Variables
Introduce variables and explain the distinction between variables
and objects. Also, explain the rules for variable construction.

### Exercise
Have students create a variable for their age and favorite number.
Print out all the result of all four mathematical operations on them.

```python3
age = 10
fav_number = 3
print(age + fav_number)
print(age - fav_number)
print(age * fav_number)
print(age / fav_number)
```

To demonstrate a variable's ability to be updated, have them update one of
the variables after the four prints, and then run the print statements again.

```python3
age = 10
fav_number = 3
print(age + fav_number)
print(age - fav_number)
print(age * fav_number)
print(age / fav_number)
age = 11
print(age + fav_number)
print(age - fav_number)
print(age * fav_number)
print(age / fav_number)
```