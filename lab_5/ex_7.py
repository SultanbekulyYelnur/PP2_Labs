import re
text = "hello_world"
words = text.split('_')
print(words[0] + ''.join(word.capitalize() for word in words[1:])) 