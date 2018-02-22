# Containers
## List Container
Introduce the list container and describe some typical usages.
Explain how lists are constructed with square brackets and commas.


### Exercise
Have students create a master list with at least five numbers in them.

```python3
master_lst = [1, 2, 3, 4, 5]
print ('My master list is {}'.format(master_lst))
```

## List Length
Introduce students to the **len** function.

### Exercise
Have students extend the previous exercise by printing out the size of their
list.

```python3
master_lst = [1, 2, 3, 4, 5]
print ('My master list is {}'.format(master_lst))
print ('It has {} values'.format(len(master_lst)))
```

## List Append
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

## List Indexing
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

## List Addition
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

## Dictionary Container
Introduce the dictionary container and describe some typical usages.
Explain how dictionaries are constructed with curly braces, colons and commas.

### Exercise
Have students create a single entry dictionary of their favorite color.
The key will be their name, and the value will their favorite color.

```python3
fav_colors = {'Yaneury': 'Red'}

```

## Dictionary Key Access
Explain how value retrieval is done by using the key on the dictionary.

### Exercise
Extend the previous exercise by having students get the user's name and storing
it in a variable. Then, using dictionary key access, have the students print
out their favorite color. Then, ask the user for their favorite color,  

```python3
fav_colors = {'Yaneury': 'Red'}

name = input('What is your name? ')
color = input('My favorite color is {}. What is yours?'.format(fav_colors['Yaneury']))
```

## Dictionary Key Insertion and Update
Explain how key-value insertion/update is done.

### Exercise
Extend the previous exercise by having students insert into the dictionary the
user's favorite color.

```python3
fav_colors = {'Yaneury': 'Red'}

name = input('What is your name? ')
color = input('My favorite color is {}. What is yours?'.format(fav_colors['Yaneury']))
fav_colors[name] = color

print (fav_colors)
```

## Dictionary Key Deletion
Briefly touch on key-value deletion.

## For Loops with Lists
Introduce students to for loops using the lists (not range).

### Exercise
Have students make as big a list as possible. Instruct them to create
a for loop that prints each element in the list.

```python3
lst = [1, 3.14, "john"]
for el in lst:
    print (el)
```

## For Loops with Range
Introduce students to creating for loops with the range function.
Show them how range works outside of a for loop.


### Exercise
Have students get a number **n** from user input. Loop **n** times and print
each number from 0 to **n - 1**.

```python3
n = int(input('Number: '))
for i in range(n):
    print (i)
```

## For Loops with Dictionaries
Introduce students to dictionary-based for loops.

### Exercise
Have students extend on the favorite color exercise by looping 
each name-color pair and printing it.

```python3
fav_colors = {'Yaneury': 'Red'}

name = input('What is your name? ')
color = input('My favorite color is {}. What is yours?'.format(fav_colors['Yaneury']))
fav_colors[name] = color

for name in fav_colors:
    print ('{} - {}'.format(name, fav_colors[name]))
```