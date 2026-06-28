import re

with open('index.html', 'r') as f:
    content = f.read()

# 2. Fix extra space in calc-tool-result
css_search = '.calc-tool-result{min-height:42px;'
css_replace = '.calc-tool-result{min-height:0;'
if css_search in content:
    content = content.replace(css_search, css_replace)

# 3. Align calculate button with inputs (remove margin-bottom: 2px)
html_btn_search = 'margin-bottom:2px;'
html_btn_replace = 'margin-bottom:0;'
if html_btn_search in content:
    content = content.replace(html_btn_search, html_btn_replace)

# 4. Hide panel when app is backgrounded
js_vis_search = "let CALC_PERCENT_TOOL='';"
js_vis_replace = "let CALC_PERCENT_TOOL='';\ndocument.addEventListener('visibilitychange', () => { if(document.visibilityState === 'hidden' && CALC_PERCENT_TOOL) toggleCalcPercentTool(CALC_PERCENT_TOOL); });"
if js_vis_search in content:
    content = content.replace(js_vis_search, js_vis_replace)

# 5. Make close button smaller and reduce top bar margin
top_bar_search = '.calc-top-bar { display:flex; align-items:center; justify-content:space-between; margin-top:10px; margin-bottom:12px; padding:0 4px; }'
top_bar_replace = '.calc-top-bar { display:flex; align-items:center; justify-content:space-between; margin-top:6px; margin-bottom:4px; padding:0 4px; }'
if top_bar_search in content:
    content = content.replace(top_bar_search, top_bar_replace)

close_btn_search = '.calc-close-btn{display:inline-flex;align-items:center;justify-content:center;padding:4px 12px;min-height:28px;'
close_btn_replace = '.calc-close-btn{display:inline-flex;align-items:center;justify-content:center;padding:2px 10px;min-height:22px;'
if close_btn_search in content:
    content = content.replace(close_btn_search, close_btn_replace)

# Bump version text to v36
content = content.replace('>v35</div>', '>v36</div>')

with open('index.html', 'w') as f:
    f.write(content)

