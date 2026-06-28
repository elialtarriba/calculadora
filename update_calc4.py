import re

with open('index.html', 'r') as f:
    content = f.read()

css_search = '.calc-tool-button{position:relative;overflow:hidden;flex:1;padding:12px 6px;font-size:clamp(10px,3vw,13px);font-weight:800;color:#151515;background:linear-gradient(180deg,var(--calc-tool-btn-top,rgba(255,255,255,.8)),var(--calc-tool-btn-bottom,rgba(255,255,255,.5)));border:1px solid rgba(255,255,255,.5);border-radius:10px;cursor:pointer;box-shadow:0 4px 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),0 6px 10px rgba(0,0,0,.15),inset 0 1px 0 rgba(255,255,255,.8)}.calc-tool-button:active{transform:translateY(4px);box-shadow:0 0 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),inset 0 2px 4px rgba(0,0,0,.15)}'

css_replace = '.calc-tool-button{position:relative;overflow:hidden;flex:1;padding:12px 6px;font-size:clamp(10px,3vw,13px);font-weight:800;color:#151515;background:linear-gradient(180deg,var(--calc-tool-btn-top,rgba(255,255,255,.8)),var(--calc-tool-btn-bottom,rgba(255,255,255,.5)));border:1px solid rgba(255,255,255,.5);border-radius:10px;cursor:pointer;box-shadow:0 8px 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-tool-button::before{content:\'\';position:absolute;top:12%;left:16%;right:16%;bottom:12%;border-radius:40%;box-shadow:inset 0 4px 6px rgba(0,0,0,.08),inset 0 -4px 6px rgba(255,255,255,.3);background:radial-gradient(ellipse at center,rgba(0,0,0,.04) 0%,transparent 70%);pointer-events:none;transition:opacity .15s}.calc-tool-button:active, .calc-tool-button.active{transform:translateY(8px);box-shadow:0 0 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),inset 0 3px 5px rgba(0,0,0,.2)}.calc-tool-button:active::before, .calc-tool-button.active::before{opacity:0.4}'

if css_search in content:
    content = content.replace(css_search, css_replace)
else:
    print("WARNING: css search block not found")

# Bump version text to v30
content = content.replace('>v29</div>', '>v30</div>')

with open('index.html', 'w') as f:
    f.write(content)

