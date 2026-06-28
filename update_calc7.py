import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace panel html block
old_panel_html = """  <div class="calc-tool-panel" id="calc-percent-panel">
    <div class="calc-tool-fields">
      <div class="calc-tool-field"><label for="calc-tool-amount">Importe</label><input type="text" inputmode="decimal" id="calc-tool-amount" placeholder="100,00"></div>
      <div class="calc-tool-field"><label for="calc-tool-percent" id="calc-tool-percent-label">Porcentaje %</label><input type="text" inputmode="decimal" id="calc-tool-percent" placeholder="20"></div>
    </div>
    <div style="display:flex; gap:10px; margin-top:10px;">
      <button class="calc-tool-calculate" style="margin-top:0; width:100px; flex-shrink:0;" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_calc_btn'); } else calculateCalcPercentTool()">Calcular</button>
      <div class="calc-tool-result" id="calc-tool-result" style="margin-top:0; flex-grow:1; display:flex; align-items:center; font-size:12px; padding:6px 11px; line-height:1.2;">Escribe el importe y el porcentaje.</div>
    </div>
  </div>"""

new_panel_html = """  <div class="calc-tool-panel" id="calc-percent-panel">
    <div style="display:flex; gap:8px; align-items:flex-end; margin-bottom:10px;">
      <button class="calc-tool-calculate" style="margin-top:0; width:80px; flex-shrink:0; height:42px; margin-bottom:2px; font-size:13px; padding: 0;" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_calc_btn'); } else calculateCalcPercentTool()">Calcular</button>
      <div class="calc-tool-fields" style="flex-grow:1; display:grid; grid-template-columns:1fr 1fr; gap:8px;">
        <div class="calc-tool-field"><label for="calc-tool-amount">Importe</label><input type="text" inputmode="decimal" id="calc-tool-amount" placeholder="100,00" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); }"></div>
        <div class="calc-tool-field"><label for="calc-tool-percent" id="calc-tool-percent-label">Porcentaje %</label><input type="text" inputmode="decimal" id="calc-tool-percent" placeholder="20" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); }"></div>
      </div>
    </div>
    <div class="calc-tool-result" id="calc-tool-result" style="margin-top:0; font-size:11px; padding:6px 11px; line-height:1.2; text-align:center;">Escribe el importe y el porcentaje.</div>
  </div>"""

if old_panel_html in content:
    content = content.replace(old_panel_html, new_panel_html)
else:
    print("WARNING: panel html not found")

# Bump version text to v32
content = content.replace('>v31</div>', '>v32</div>')

with open('index.html', 'w') as f:
    f.write(content)

