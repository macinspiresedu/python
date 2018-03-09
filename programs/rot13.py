text = input("Please enter what you want me to translate: ")

result = ''
for c in text:
    if c >= 'a' and c <= 'z':
        result += chr(((ord(c) - ord('a') + 13) % 26) + ord('a'))
    elif c >= 'A' and c <= 'Z':
        result += chr(((ord(c) - ord('A') + 13) % 26) + ord('A'))
    else:
        result += c

print (result)