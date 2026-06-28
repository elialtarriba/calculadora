import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add ::before styling to .calc-tool-calculate
css_search = '.calc-tool-calculate:active{transform:translateY(8px);box-shadow:0 0 0 var(--calc-tool-calc-shadow,var(--calc-accent-dark)),inset 0 3px 5px rgba(0,0,0,.2)}'
css_replace = css_search + '.calc-tool-calculate::before{content:\'\';position:absolute;top:12%;left:16%;right:16%;bottom:12%;border-radius:40%;box-shadow:inset 0 4px 6px rgba(0,0,0,.08),inset 0 -4px 6px rgba(255,255,255,.3);background:radial-gradient(ellipse at center,rgba(0,0,0,.04) 0%,transparent 70%);pointer-events:none;transition:opacity .15s}.calc-tool-calculate:active::before{opacity:0.4}'
content = content.replace(css_search, css_replace)

# 2. Update HTML layout for calc-tool-calculate and calc-tool-result
html_search = """    <button class="calc-tool-calculate" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_calc_btn'); } else calculateCalcPercentTool()">Calcular</button>
    <div class="calc-tool-result" id="calc-tool-result">Escribe el importe y el porcentaje.</div>"""

html_replace = """    <div style="display:flex; gap:10px; margin-top:10px;">
      <button class="calc-tool-calculate" style="margin-top:0; width:100px; flex-shrink:0;" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_calc_btn'); } else calculateCalcPercentTool()">Calcular</button>
      <div class="calc-tool-result" id="calc-tool-result" style="margin-top:0; flex-grow:1; display:flex; align-items:center; font-size:12px; padding:6px 11px; line-height:1.2;">Escribe el importe y el porcentaje.</div>
    </div>"""

if html_search in content:
    content = content.replace(html_search, html_replace)
else:
    print("WARNING: html layout block not found")

# 3. Bump version text to v29
content = content.replace('>v28</div>', '>v29</div>')

with open('index.html', 'w') as f:
    f.write(content)

