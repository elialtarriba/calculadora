import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix the shadow darkness on the tool buttons
old_shadow_logic = '50%,#000)'
new_shadow_logic = '75%,#000)'
content = content.replace(old_shadow_logic, new_shadow_logic)

# Also fix the default background logic to not be so solid if not set
old_top_logic = '60%,#FFF)'
new_top_logic = '80%,#FFF)'
content = content.replace(old_top_logic, new_top_logic)

# Bump version text to v42
content = content.replace('>v41</div>', '>v42</div>')

with open('index.html', 'w') as f:
    f.write(content)

