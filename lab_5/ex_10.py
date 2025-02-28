import re
text = "HelloWorldTest"
print(re.sub(r'(?<!^)([A-Z])', r'_\1', text).lower())