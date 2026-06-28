import re

with open('index.html', 'r') as f:
    content = f.read()

# Current buggy CSS block for special keys
css_search = '.calc-key.op{background:linear-gradient(180deg,var(--calc-op-top),var(--calc-op-bottom));box-shadow:0 8px 0 var(--calc-op-shadow),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-key.clear{background:linear-gradient(180deg,var(--calc-clear-top),var(--calc-clear-bottom));box-shadow:0 8px 0 var(--calc-clear-shadow),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-key.top-op{background:linear-gradient(180deg,var(--calc-top-op-top, var(--calc-clear-top)),var(--calc-top-op-bottom, var(--calc-clear-bottom)));box-shadow:0 8px 0 var(--calc-top-op-shadow, var(--calc-clear-shadow)),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-key.equals{background:linear-gradient(180deg,color-mix(in srgb,var(--calc-accent) 55%,#fff 45%),var(--calc-accent));box-shadow:0 8px 0 var(--calc-accent-dark),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}'

css_replace = '.calc-key.op{background:linear-gradient(180deg,var(--calc-op-top),var(--calc-op-bottom));box-shadow:0 8px 0 var(--calc-op-shadow),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-key.op:active{box-shadow:0 0 0 var(--calc-op-shadow),inset 0 3px 5px rgba(0,0,0,.2)}.calc-key.clear{background:linear-gradient(180deg,var(--calc-clear-top),var(--calc-clear-bottom));box-shadow:0 8px 0 var(--calc-clear-shadow),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-key.clear:active{box-shadow:0 0 0 var(--calc-clear-shadow),inset 0 3px 5px rgba(0,0,0,.2)}.calc-key.top-op{background:linear-gradient(180deg,var(--calc-top-op-top, var(--calc-clear-top)),var(--calc-top-op-bottom, var(--calc-clear-bottom)));box-shadow:0 8px 0 var(--calc-top-op-shadow, var(--calc-clear-shadow)),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-key.top-op:active{box-shadow:0 0 0 var(--calc-top-op-shadow, var(--calc-clear-shadow)),inset 0 3px 5px rgba(0,0,0,.2)}.calc-key.equals{background:linear-gradient(180deg,color-mix(in srgb,var(--calc-accent) 55%,#fff 45%),var(--calc-accent));box-shadow:0 8px 0 var(--calc-accent-dark),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-key.equals:active{box-shadow:0 0 0 var(--calc-accent-dark),inset 0 3px 5px rgba(0,0,0,.2)}'

if css_search in content:
    content = content.replace(css_search, css_replace)
else:
    print("WARNING: css block not found")

# Bump version text to v31
content = content.replace('>v30</div>', '>v31</div>')

with open('index.html', 'w') as f:
    f.write(content)

