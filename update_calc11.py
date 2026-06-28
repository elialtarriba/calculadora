import re

with open('index.html', 'r') as f:
    content = f.read()

# Let's add flex-shrink: 0 to calculator-display just in case it's shrinking and causing visual cutoff
css_search = '.calculator-display{min-height:124px;'
css_replace = '.calculator-display{flex-shrink:0;min-height:124px;'

if css_search in content:
    content = content.replace(css_search, css_replace)

# Also let's ensure the calculator grid can shrink properly
# And let's make sure the calc-tool-panel doesn't overflow.
# Actually, the issue might be that the calculator-shell needs overflow-y: auto instead of hidden body?
# If the screen is too small to fit the panel + grid, it MUST scroll! Otherwise something gets cut off.
# Let's change body overflow:hidden to overflow-y:auto or make calculator-shell overflow-y:auto
body_search = "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;background:#f5ead8;color:#3a2810;height:100vh;display:flex;flex-direction:column;overflow:hidden;}"
body_replace = "body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;background:#f5ead8;color:#3a2810;height:100vh;display:flex;flex-direction:column;overflow-x:hidden;overflow-y:auto;}"

if body_search in content:
    content = content.replace(body_search, body_replace)

# Bump version text to v35
content = content.replace('>v34</div>', '>v35</div>')

with open('index.html', 'w') as f:
    f.write(content)

