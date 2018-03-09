NEED_NOUN = 1
NEED_ADJECTIVE = 2
NEED_PLURAL_NOUN = 3
NEED_ADVERB = 4

stories = [
    [NEED_NOUN, 'The wolf went into the {}'],
    [NEED_ADVERB, 'Rudolf {} flew across the Earth!'],
]

result = []

for story in stories:
    phrase_needed = story[0]
    phrase = ''
    if phrase_needed == NEED_NOUN:
        phrase = input('Please input a noun: ')
    elif phrase_needed == NEED_ADJECTIVE:
        phrase = input('Please input an adjective: ')
    elif phrase_needed == NEED_ADVERB:
        phrase = input('Please input an adverb: ')
    else:
        phrase = input('Please input a plural noun: ')
    result.append(story[1].format(phrase))

for story in result:
    print (story)