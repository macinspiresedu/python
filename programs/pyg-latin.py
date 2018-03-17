pyg = 'ay'
word = input('Please input a word: ')

if len(word) > 0 and word.isalpha():
    new_word = word.lower()
    first = new_word[0]
    new_word = new_word + first + pyg
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print ('Invalid input!')
