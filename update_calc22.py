import re

with open('index.html', 'r') as f:
    content = f.read()

# Bump version text to v43
content = content.replace('>v42</div>', '>v43</div>')

with open('index.html', 'w') as f:
    f.write(content)

