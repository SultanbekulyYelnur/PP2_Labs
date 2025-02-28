import re
text = "hello, world. test"
print(re.sub(r'[ ,.]', ':', text))