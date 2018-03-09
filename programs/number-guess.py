from random import randint

lower_bound = 1
upper_bound = 100
random_number = randint(lower_bound, upper_bound)
n = int(input("Hey! I'm thinking of a number between {} and {}. Can you guess what it is: ".format(lower_bound, upper_bound)))
attempts = 1
while n != random_number:
    if n > random_number:
        print ("Too high!")
    else:
        print ("Too low!")
     
    attempts += 1
    n = int(input("Guess again: "))

if attempts == 1:
    print ("Wow! You got it in one try!")
else:
    print ("You finally got it! It only took {} tries!".format(attempts))    