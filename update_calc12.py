import re

with open('index.html', 'r') as f:
    content = f.read()

# Change calculator-shell to min-height instead of fixed height
shell_search = 'width:100vw; height:100vh; padding:env(safe-area-inset-top, 40px) 20px env(safe-area-inset-bottom, 40px) 20px; box-sizing:border-box;'
shell_replace = 'width:100vw; min-height:100vh; padding:env(safe-area-inset-top, 40px) 20px env(safe-area-inset-bottom, 40px) 20px; box-sizing:border-box;'

if shell_search in content:
    content = content.replace(shell_search, shell_replace)
else:
    print("WARNING: shell search not found")

with open('index.html', 'w') as f:
    f.write(content)

