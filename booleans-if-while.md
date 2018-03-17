## Booleans
Introduce the boolean type and describe some typical usages
(equality testing, etc.). Also, explain how boolean expressions can
be constructed with comparison operators, boolean operators and
'True' or 'False'.

### Exercise
Run the program under [tests/boolean-test.py](https://github.com/macinspiresedu/python/blob/master/tests/boolean-test.py) on repl.it. Project it onto a big
screen or have the students huddle around a single computer. This program will
test their understanding of boolean expressions. Have them try to answer the
questions and explain any wrong or right answer.

## If
Go over if statements usage and constructions. 
Connect it with the boolean expressions that they previously practiced. Go over else-if and else statements as well.

### Exercise
Have the students write a script that asks the user for their age and compares against the student's age.
For each case (ages are equal, user's age is greater, student's age is greater) have them print out a statement.

#### Age Comparison

```python3
my_age = 10

user_age = int(input("Hey there. I'm {} years old. How about you? ".format(my_age)))

if my_age == user_age:
    print ("Hey we have the same age!")
elif my_age > user_age:
    print ("Hey I'm older than you!")
else:
    print ("Hey I'm younger than you!")

```

#### Morse Code
At this point the students should have enough knowledge to build a simple
morse code translator. Review the contents of [programs/morse-code.py](https://github.com/macinspiresedu/python/blob/master/programs/morse-code.py) to
see a sample solution. Any new material needed (like the .upper() and 'in') should
be reviewed before the students tackle on developing their own solution. Help them develop
the translator and don't be too restrictive as to what they can and to how they'll build it.
If they use inefficient methods, use it as a teaching moment to describe a better way to do it.

## While
<<<<<<< HEAD
Introduce students to while loops and explain the difference between while loops
and for loops. 

### Fun Programs
At this point, the students should be to work on the number
guessing game. A sample solution for that challenge can be found under programs/number-guess.py
Briefly introduce the 'random' module. Hiding away the details about how 'import'
works. Focus on explaining that they can use 'random.randint' to get a random
number.

Another program that the students are able to develop at this point is the
Rot13 translator. Briefly explain the ord() and chr() functions before asking
them to implement it. A sample solution can be found under programs/rot13.py.

A third program that the students can work on is the Mad Libs generator program.
A sample solution of this can be found programs/mad-libs.py.
=======
TBD

### Exercise
>>>>>>> 3ed49fc8b4b176a86f248ed91f2c8a05fc2b8094
