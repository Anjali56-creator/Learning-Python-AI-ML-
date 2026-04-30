import re

text = "Hello, my email is user@example.com"

# Search for a pattern
match = re.search(r'\w+@\w+\.\w+', text)
if match:
    print(match.group()) 