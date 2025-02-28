import re
text = "HelloWorldTest"
print(re.sub(r'(?<!^)([A-Z])', r' \1', text))