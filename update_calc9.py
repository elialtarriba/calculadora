import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace('>v32</div>', '>v33</div>')

with open('index.html', 'w') as f:
    f.write(content)

