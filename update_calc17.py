import re

with open('index.html', 'r') as f:
    content = f.read()

# Bump version text to v38
content = content.replace('>v37</div>', '>v38</div>')

with open('index.html', 'w') as f:
    f.write(content)

