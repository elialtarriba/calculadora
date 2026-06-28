import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. More margin-bottom for calc-top-bar (Salir button)
top_bar_search = '.calc-top-bar { display:flex; align-items:center; justify-content:space-between; margin-top:6px; margin-bottom:4px; padding:0 4px; }'
top_bar_replace = '.calc-top-bar { display:flex; align-items:center; justify-content:space-between; margin-top:6px; margin-bottom:16px; padding:0 4px; }'
if top_bar_search in content:
    content = content.replace(top_bar_search, top_bar_replace)

# 2. Fix align-items for Calculate button (add 8px margin-bottom to compensate for box-shadow)
btn_search = '<button class="calc-tool-calculate" style="margin-top:0; width:80px; flex-shrink:0; height:42px; margin-bottom:0; font-size:13px; padding: 0;"'
btn_replace = '<button class="calc-tool-calculate" style="margin-top:0; width:80px; flex-shrink:0; height:42px; margin-bottom:8px; font-size:13px; padding: 0;"'
if btn_search in content:
    content = content.replace(btn_search, btn_replace)

# 3. Enable robust scrolling on calculator-shell for iOS
# Change calculator-shell to height: 100dvh and add overflow-y: auto
shell_search = 'width:100vw; min-height:100vh; padding:env(safe-area-inset-top, 40px) 20px env(safe-area-inset-bottom, 40px) 20px; box-sizing:border-box;'
shell_replace = 'width:100%; height:100dvh; min-height:100vh; overflow-y:auto; overflow-x:hidden; -webkit-overflow-scrolling:touch; padding:env(safe-area-inset-top, 40px) 20px env(safe-area-inset-bottom, 40px) 20px; box-sizing:border-box;'
if shell_search in content:
    content = content.replace(shell_search, shell_replace)
else:
    # try the other one if not found
    shell_search2 = 'width:100vw; height:100vh; padding:env(safe-area-inset-top, 40px) 20px env(safe-area-inset-bottom, 40px) 20px; box-sizing:border-box;'
    if shell_search2 in content:
        content = content.replace(shell_search2, shell_replace)

# Bump version text to v39
content = content.replace('>v38</div>', '>v39</div>')

with open('index.html', 'w') as f:
    f.write(content)

