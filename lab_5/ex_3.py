import re
text = "hello_world test_case example_text"
print(re.findall(r'\b[a-z]+_[a-z]+\b', text))  