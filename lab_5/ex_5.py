import re
text = "a123b"
print(bool(re.fullmatch(r'a.*b', text)))