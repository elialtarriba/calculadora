import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add readonly and active tool input logic to HTML
html_search = """        <div class="calc-tool-field"><label for="calc-tool-amount">Importe</label><input type="text" inputmode="decimal" id="calc-tool-amount" placeholder="100,00" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); }"></div>
        <div class="calc-tool-field"><label for="calc-tool-percent" id="calc-tool-percent-label">Porcentaje %</label><input type="text" inputmode="decimal" id="calc-tool-percent" placeholder="20" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); }"></div>"""

html_replace = """        <div class="calc-tool-field"><label for="calc-tool-amount">Importe</label><input type="text" readonly id="calc-tool-amount" placeholder="100,00" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); } else { setActiveToolInput('amount'); }"></div>
        <div class="calc-tool-field"><label for="calc-tool-percent" id="calc-tool-percent-label">Porcentaje %</label><input type="text" readonly id="calc-tool-percent" placeholder="20" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); } else { setActiveToolInput('percent'); }"></div>"""

if html_search in content:
    content = content.replace(html_search, html_replace)
else:
    print("WARNING: input fields HTML not found")

# 2. Add ACTIVE_TOOL_INPUT variable
vars_search = "let CALC_PERCENT_TOOL='';"
vars_replace = "let CALC_PERCENT_TOOL='';\nlet ACTIVE_TOOL_INPUT=null;"
if vars_search in content:
    content = content.replace(vars_search, vars_replace)

# 3. Add setActiveToolInput function and logic to toggleCalcPercentTool
js_search = """  if(label)label.textContent=CALC_PERCENT_TOOL==='vat'?'IVA %':'Porcentaje %';
  if(result)result.textContent=CALC_PERCENT_TOOL==='vat'?'Escribe el precio con IVA y el porcentaje de IVA.':CALC_PERCENT_TOOL==='increase'?'Escribe el importe y el porcentaje que quieres sumar.':'Escribe el importe y el porcentaje que quieres quitar.';
}"""

js_replace = """  if(label)label.textContent=CALC_PERCENT_TOOL==='vat'?'IVA %':'Porcentaje %';
  if(result)result.textContent=CALC_PERCENT_TOOL==='vat'?'Escribe el precio con IVA y el porcentaje de IVA.':CALC_PERCENT_TOOL==='increase'?'Escribe el importe y el porcentaje que quieres sumar.':'Escribe el importe y el porcentaje que quieres quitar.';
  if(CALC_PERCENT_TOOL) setActiveToolInput('amount');
  else setActiveToolInput(null);
}
function setActiveToolInput(inputId) {
  ACTIVE_TOOL_INPUT = inputId;
  const amt = document.getElementById('calc-tool-amount');
  const pct = document.getElementById('calc-tool-percent');
  if(amt) amt.style.boxShadow = inputId === 'amount' ? '0 0 0 3px #4A90E2' : 'none';
  if(pct) pct.style.boxShadow = inputId === 'percent' ? '0 0 0 3px #4A90E2' : 'none';
}"""
if js_search in content:
    content = content.replace(js_search, js_replace)

with open('index.html', 'w') as f:
    f.write(content)
