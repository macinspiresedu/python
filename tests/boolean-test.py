prompts = [
    'len("John") == 4',
    'len("John") >= 4',
    'len("John") > 4',
    'len("John") != 4',
    '200 > len("Michael")',
    '0 > -1',
    '300 == "300"',
    '"abc" > "bac"',
    "2 > 3 or 3 > 2",
    "1 == 1 and 2 < 3",
    "2 < 3 and 3 > 4",
    "not (2 == 2)",
    "not (2 == 2 and 3 != 3)",
    "not False",
    "True and (not False)",
    "False or (not 2 > 3)",
    "False and (not 2 > 3)"
]

print ("Hey! This program will test your understanding of boolean expressions in Python!\n" +
       "For each expression, write 'True' or 'False' (without the quotes).\n" +
       "There are {} expressions. Let's see how many you get right!\n".format(len(prompts)))

ctr = 0
for p in prompts:
    given_answer = input("{}: ".format(p))
    while given_answer not in ['True', 'False']:
      given_answer = input("Please type in 'True' or 'False': ") 
    
    given_answer = given_answer == 'True'
    expected_answer = eval(p)
    if given_answer == expected_answer:
        print ("Correct!")
        ctr += 1
    else:
        print ("Wrong!")

print ()
if not ctr:
  print ("Looks like you didn't get any questions right. No worries, practice and take the challenge again!")
else:
  print ("You got {} out of {} right!".format(ctr, len(prompts)))