import re

with open('index.html', 'r') as f:
    content = f.read()

# Bump version text to v40
content = content.replace('>v39</div>', '>v40</div>')

with open('index.html', 'w') as f:
    f.write(content)

