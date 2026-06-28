import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace img tag with button containing img
html_search = '<img class="calculator-signature" src="logo_elibi.jpg" alt="EliBi" onclick="showEasterEgg()">'
html_replace = '<button class="calc-mini-key calculator-signature-btn" onclick="showEasterEgg()"><img class="calculator-signature" src="logo_elibi.jpg" alt="EliBi"></button>'
if html_search in content:
    content = content.replace(html_search, html_replace)

# Update CSS for signature
css_search = '.calculator-signature{width:104px;height:46px;margin-right:auto;object-fit:contain;mix-blend-mode:multiply;cursor:pointer;transition:all .15s;filter:drop-shadow(0 4px 0 rgba(0,0,0,.15))}'
css_replace = '.calculator-signature-btn { margin-right:auto; padding: 0 10px; display: flex; align-items: center; justify-content: center; } .calculator-signature{width:70px;height:24px;object-fit:contain;mix-blend-mode:multiply;pointer-events:none;}'
if css_search in content:
    content = content.replace(css_search, css_replace)

# Remove the active state for img since button handles it
css_active_search = '.calculator-signature:active{transform:translateY(4px);opacity:0.8;filter:drop-shadow(0 0 0 rgba(0,0,0,.15))}'
css_active_replace = ''
if css_active_search in content:
    content = content.replace(css_active_search, css_active_replace)

# Also fix the mobile responsive width rule
css_mobile_search = '.calculator-signature{width:82px}'
css_mobile_replace = '.calculator-signature{width:60px; height:20px;}'
if css_mobile_search in content:
    content = content.replace(css_mobile_search, css_mobile_replace)

# Bump version to v37
content = content.replace('>v36</div>', '>v37</div>')

with open('index.html', 'w') as f:
    f.write(content)

