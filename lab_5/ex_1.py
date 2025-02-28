import re 
text = "ab"
print(bool(re.fullmatch(r'ab*', text)))