# Containers
## Lists
### List Container
Introduce the string type and describe some typical usages.
Explain how lists are constructed with square brackets and commas.


### Exercise
Have students create a master list with at least five numbers in them.

```python3
master_lst = [1, 2, 3, 4, 5]
print ('My master list is {}'.format(master_lst))
```

### List Length
Introduce students to the **len** function.

### Exercise
Have students extend the previous exercise by printing out the size of their
list.

```python3
master_lst = [1, 2, 3, 4, 5]
print ('My master list is {}'.format(master_lst))
print ('It has {} values'.format(len(master_lst)))
```

### List Append
Introduce students to the **append** method.

### Exercise
Extend the previous exercise by having students ask the user for three numbers.
They must append each value as is it inputted into a new list.


```python3
master_lst = [1, 2, 3, 4, 5]
print ('My master list is {}'.format(master_lst))
print ('It has {} values'.format(len(master_lst)))

lst = []
print ('Give me three numbers)
lst.append(int(input('Number one: ')))
lst.append(int(input('Number two: ')))
lst.append(int(input('Number three: ')))

```

### List Indexing
Explain how list indexing works. Students should be familiar with the
syntax by now, as should have seen it when working with strings. Nevertheless,
it does not hurt to go over it again.

### Exercise
Extend the previous exercise by having students print out each of the numbers
in the list by its corresponding index. Then, print out the sum of all numbers.

```python3
master_lst = [1, 2, 3, 4, 5]
print ('My master list is {}'.format(master_lst))
print ('It has {} values'.format(len(master_lst)))

lst = []
print ('Give me three numbers)
lst.append(int(input('Number one: ')))
lst.append(int(input('Number two: ')))
lst.append(int(input('Number three: ')))

print ('Your first number: {}'.format(lst[0]))
print ('Your second number: {}'.format(lst[1]))
print ('Your third number: {}'.format(lst[2]))
sum = lst[0] + lst[1] + lst[2]
print ('The sum of your three number is {}'.format(sum))
```

### List Addition
Explain how list addition works and how it creates a new combined list.

### Exercise
Extend the previous exercise by having students creating a variable that
contains the sum of the master list and the user inputted list. Then,
print out that new list.

```python3
master_lst = [1, 2, 3, 4, 5]
print ('My master list is {}'.format(master_lst))
print ('It has {} values'.format(len(master_lst)))

lst = []
print ('Give me three numbers)
lst.append(int(input('Number one: ')))
lst.append(int(input('Number two: ')))
lst.append(int(input('Number three: ')))

print ('Your first number: {}'.format(lst[0]))
print ('Your second number: {}'.format(lst[1]))
print ('Your third number: {}'.format(lst[2]))
sum = lst[0] + lst[1] + lst[2]
print ('The sum of your three number is {}'.format(sum))

new_lst = master_lst + lst
print ('Our lists combined is {}'.format(new_lst))
```

## Tuples
### Tuple Container
Explain how similar the tuple type is to the list. Emphasize that
the only major difference is how they are constructed and that they
are immutable.


## Maps / Dictionaries

```python3

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

character = input('Input a character')
print ('The translation in morse code is {}'.format(MORSE_CODE_DICT[character]))

```
