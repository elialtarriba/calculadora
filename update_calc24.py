import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove delete button and add tooltip span
render_search = """    html += custom.map((theme,index)=>`<div style="position:relative; display:inline-block;"><button class="calc-color" title="${theme.name}" style="background:linear-gradient(135deg,${theme.accent||'#ccc'},${theme.display||'#eee'},${theme.opBottom||'#ddd'})" onclick="setCalculatorTheme(getCustomThemes()[${index}]); toggleCalculatorPalette()"></button><button onclick="deleteCustomTheme(${index}); if(typeof event!=='undefined')event.stopPropagation();" style="position:absolute; top:-6px; right:-6px; background:white; border:1px solid #ccc; border-radius:50%; width:20px; height:20px; font-size:12px; display:flex; align-items:center; justify-content:center; cursor:pointer; color:red; box-shadow:0 2px 4px rgba(0,0,0,0.2); z-index:10;">✕</button></div>`).join('');"""
render_replace = """    html += custom.map((theme,index)=>`<div class="calc-color-custom" style="position:relative; display:inline-block;"><button class="calc-color" style="background:linear-gradient(135deg,${theme.accent||'#ccc'},${theme.display||'#eee'},${theme.opBottom||'#ddd'})" onclick="setCalculatorTheme(getCustomThemes()[${index}]); toggleCalculatorPalette()"></button><span class="calc-color-tooltip">${theme.name}</span></div>`).join('');"""

if render_search in content:
    content = content.replace(render_search, render_replace)
else:
    print("Warning: renderThemes html replace failed")

# 2. Add tooltip CSS
css_search = ".calc-color:active { transform:translateY(2px); }"
css_replace = ".calc-color:active { transform:translateY(2px); }\n.calc-color-tooltip { position:absolute; bottom:115%; left:50%; transform:translateX(-50%); background:rgba(0,0,0,0.7); color:#fff; padding:4px 8px; border-radius:6px; font-size:11px; font-weight:600; white-space:nowrap; pointer-events:none; opacity:0; transition:opacity 0.2s; z-index:100; box-shadow:0 2px 6px rgba(0,0,0,0.2); }\n.calc-color-custom:hover .calc-color-tooltip, .calc-color-custom:active .calc-color-tooltip { opacity:1; }"
if css_search in content:
    content = content.replace(css_search, css_replace)

# Bump version to v45
content = content.replace('>v44</div>', '>v45</div>')

with open('index.html', 'w') as f:
    f.write(content)

