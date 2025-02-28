import re
text = "abb"
print(bool(re.fullmatch(r'ab{2,3}', text)))