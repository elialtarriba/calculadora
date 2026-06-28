import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update .calc-tool-button borders and ::before positioning
css_search = '.calc-tool-button{position:relative;overflow:hidden;flex:1;padding:12px 6px;font-size:clamp(10px,3vw,13px);font-weight:800;color:#151515;background:linear-gradient(180deg,var(--calc-tool-btn-top,rgba(255,255,255,.8)),var(--calc-tool-btn-bottom,rgba(255,255,255,.5)));border:1px solid rgba(255,255,255,.5);border-radius:10px;cursor:pointer;box-shadow:0 8px 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}.calc-tool-button::before{content:\'\';position:absolute;top:12%;left:16%;right:16%;bottom:12%;border-radius:40%;box-shadow:inset 0 4px 6px rgba(0,0,0,.08),inset 0 -4px 6px rgba(255,255,255,.3);background:radial-gradient(ellipse at center,rgba(0,0,0,.04) 0%,transparent 70%);pointer-events:none;transition:opacity .15s}'
css_replace = '.calc-tool-button{position:relative;overflow:hidden;flex:1;padding:12px 6px;font-size:clamp(10px,3vw,13px);font-weight:800;color:#151515;background:linear-gradient(180deg,var(--calc-tool-btn-top,rgba(255,255,255,.8)),var(--calc-tool-btn-bottom,rgba(255,255,255,.5)));border:1px solid rgba(0,0,0,.2);border-radius:10px;cursor:pointer;box-shadow:0 8px 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),0 11px 15px rgba(0,0,0,.26),inset 0 0 0 1px rgba(255,255,255,.6),inset 0 2px 1px rgba(255,255,255,.95)}.calc-tool-button::before{content:\'\';position:absolute;top:16%;left:16%;right:16%;bottom:8%;border-radius:40%;box-shadow:inset 0 4px 6px rgba(0,0,0,.08),inset 0 -4px 6px rgba(255,255,255,.3);background:radial-gradient(ellipse at center,rgba(0,0,0,.04) 0%,transparent 70%);pointer-events:none;transition:opacity .15s}'
if css_search in content:
    content = content.replace(css_search, css_replace)
else:
    print("WARNING: tool button css not found")

# 2. Update HTML layout for the panel
html_search = """    <div style="display:flex; gap:10px; margin-top:10px;">
      <button class="calc-tool-calculate" style="margin-top:0; width:100px; flex-shrink:0;" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_calc_btn'); } else calculateCalcPercentTool()">Calcular</button>
      <div class="calc-tool-result" id="calc-tool-result" style="margin-top:0; flex-grow:1; display:flex; align-items:center; font-size:12px; padding:6px 11px; line-height:1.2;">Escribe el importe y el porcentaje.</div>
    </div>"""

# Remove the old layout parts (including calc-tool-fields which is right before this)
old_panel_html = """  <div class="calc-tool-panel" id="calc-percent-panel">
    <div class="calc-tool-fields">
      <div class="calc-tool-field"><label for="calc-tool-amount">Importe</label><input type="text" inputmode="decimal" id="calc-tool-amount" placeholder="100,00" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); }"></div>
      <div class="calc-tool-field"><label for="calc-tool-percent" id="calc-tool-percent-label">Porcentaje %</label><input type="text" inputmode="decimal" id="calc-tool-percent" placeholder="20" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('toolpanel_inputs'); }"></div>
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

# 3. Update calculateCalcPercentTool logic
js_search = """function calculateCalcPercentTool(){
  const amount=calcToolNumber(document.getElementById('calc-tool-amount')?.value),percent=calcToolNumber(document.getElementById('calc-tool-percent')?.value),result=document.getElementById('calc-tool-result');
  if(!result||!CALC_PERCENT_TOOL)return;if(!Number.isFinite(amount)||!Number.isFinite(percent)||amount<0||percent<0){result.textContent='Introduce un importe y un porcentaje válidos.';return;}calcBeep();
  if(CALC_PERCENT_TOOL==='discount'){const removed=amount*percent/100;result.innerHTML=`<strong>Resultado: ${calcMoney(amount-removed)} €</strong><br>Se quitan ${calcMoney(removed)} € (${formatCalcValue(percent)} %).`;return;}
  if(CALC_PERCENT_TOOL==='increase'){const added=amount*percent/100;result.innerHTML=`<strong>Resultado: ${calcMoney(amount+added)} €</strong><br>Se suman ${calcMoney(added)} € (${formatCalcValue(percent)} %).`;return;}
  const net=amount/(1+percent/100);result.innerHTML=`<strong>Sin IVA: ${calcMoney(net)} €</strong><br>IVA incluido: ${calcMoney(amount-net)} € (${formatCalcValue(percent)} %).`;
}"""

js_replace = """function calculateCalcPercentTool(){
  const amount=calcToolNumber(document.getElementById('calc-tool-amount')?.value),percent=calcToolNumber(document.getElementById('calc-tool-percent')?.value),result=document.getElementById('calc-tool-result');
  if(!result||!CALC_PERCENT_TOOL)return;if(!Number.isFinite(amount)||!Number.isFinite(percent)||amount<0||percent<0){result.textContent='Introduce un importe y un porcentaje válidos.';return;}calcBeep();
  let finalAmount = 0; let explanation = ''; let historyExpr = '';
  if(CALC_PERCENT_TOOL==='discount'){
    const removed=amount*percent/100; finalAmount=amount-removed;
    explanation=`Se han quitado ${calcMoney(removed)} € (${formatCalcValue(percent)} %).`;
    historyExpr = `${formatCalcValue(amount)} - ${formatCalcValue(percent)}%`;
  }
  else if(CALC_PERCENT_TOOL==='increase'){
    const added=amount*percent/100; finalAmount=amount+added;
    explanation=`Se han sumado ${calcMoney(added)} € (${formatCalcValue(percent)} %).`;
    historyExpr = `${formatCalcValue(amount)} + ${formatCalcValue(percent)}%`;
  }
  else {
    finalAmount=amount/(1+percent/100);
    explanation=`IVA incluido extraído: ${calcMoney(amount-finalAmount)} € (${formatCalcValue(percent)} %).`;
    historyExpr = `Sin IVA (${formatCalcValue(percent)}%) de ${formatCalcValue(amount)}`;
  }
  result.innerHTML = explanation;
  calcCurrentValue = String(finalAmount); calcPreviousValue = ''; calcOperator = null; calcNewNumber = true;
  updateCalc();
  if (typeof addToHistory === 'function') addToHistory(historyExpr, finalAmount);
}"""

if js_search in content:
    content = content.replace(js_search, js_replace)
else:
    print("WARNING: calc tool js not found")

# Bump version text to v32
content = content.replace('>v31</div>', '>v32</div>')

with open('index.html', 'w') as f:
    f.write(content)

