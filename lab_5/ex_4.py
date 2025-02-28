import re
text = "Hello world This Is A Test"
print(re.findall(r'\b[A-Z][a-z]+\b', text))