import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update edit-top-bar to add save button
content = content.replace(
    '<input type="color" id="edit-color-picker" oninput="if(isEditMode) applyCustomColor(currentEditType, this.value)" style="width:48px; height:48px; border:3px solid white; border-radius:10px; background:white; cursor:pointer; padding:0;">',
    '<div style="display:flex; align-items:center; gap:12px;"><button onclick="saveCustomTheme()" style="background:#fff; color:#4A90E2; border:none; padding:8px 12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">💾 Guardar</button><input type="color" id="edit-color-picker" oninput="if(isEditMode) applyCustomColor(currentEditType, this.value)" style="width:48px; height:48px; border:3px solid white; border-radius:10px; background:white; cursor:pointer; padding:0;"></div>'
)

# 2. Update tool button CSS to be 3D and support individual colors
content = content.replace(
    '.calc-tool-button{flex:1;padding:12px 6px;font-size:clamp(10px,3vw,13px);font-weight:800;color:#2E241E;background:var(--calc-tool-btn, rgba(255,255,255,.5));border:1px solid rgba(0,0,0,.1);border-radius:8px;cursor:pointer;box-shadow:0 2px 0 rgba(0,0,0,.05);position:relative}.calc-tool-button:active{background:var(--calc-tool-btn, rgba(255,255,255,.8));box-shadow:0 0 0 rgba(0,0,0,.05);transform:translateY(2px)}',
    '.calc-tool-button{position:relative;overflow:hidden;flex:1;padding:12px 6px;font-size:clamp(10px,3vw,13px);font-weight:800;color:#151515;background:linear-gradient(180deg,var(--calc-tool-btn-top,rgba(255,255,255,.8)),var(--calc-tool-btn-bottom,rgba(255,255,255,.5)));border:1px solid rgba(255,255,255,.5);border-radius:10px;cursor:pointer;box-shadow:0 4px 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),0 6px 10px rgba(0,0,0,.15),inset 0 1px 0 rgba(255,255,255,.8)}.calc-tool-button:active{transform:translateY(4px);box-shadow:0 0 0 var(--calc-tool-btn-shadow,rgba(0,0,0,.1)),inset 0 2px 4px rgba(0,0,0,.15)}\n#calc-discount-button{--calc-tool-btn-top:color-mix(in srgb,var(--calc-tool-btn-discount,#FFF) 60%,#FFF);--calc-tool-btn-bottom:var(--calc-tool-btn-discount,rgba(255,255,255,.5));--calc-tool-btn-shadow:color-mix(in srgb,var(--calc-tool-btn-discount,rgba(0,0,0,.1)) 50%,#000);}\n#calc-increase-button{--calc-tool-btn-top:color-mix(in srgb,var(--calc-tool-btn-increase,#FFF) 60%,#FFF);--calc-tool-btn-bottom:var(--calc-tool-btn-increase,rgba(255,255,255,.5));--calc-tool-btn-shadow:color-mix(in srgb,var(--calc-tool-btn-increase,rgba(0,0,0,.1)) 50%,#000);}\n#calc-vat-button{--calc-tool-btn-top:color-mix(in srgb,var(--calc-tool-btn-vat,#FFF) 60%,#FFF);--calc-tool-btn-bottom:var(--calc-tool-btn-vat,rgba(255,255,255,.5));--calc-tool-btn-shadow:color-mix(in srgb,var(--calc-tool-btn-vat,rgba(0,0,0,.1)) 50%,#000);}'
)

# 3. Update HTML for the 3 buttons
content = content.replace(
    'handleEditModeSelect(\'toolbtn\'); } else toggleCalcPercentTool(\'discount\')',
    'handleEditModeSelect(\'toolbtn_discount\'); } else toggleCalcPercentTool(\'discount\')'
).replace(
    'handleEditModeSelect(\'toolbtn\'); } else toggleCalcPercentTool(\'increase\')',
    'handleEditModeSelect(\'toolbtn_increase\'); } else toggleCalcPercentTool(\'increase\')'
).replace(
    'handleEditModeSelect(\'toolbtn\'); } else toggleCalcPercentTool(\'vat\')',
    'handleEditModeSelect(\'toolbtn_vat\'); } else toggleCalcPercentTool(\'vat\')'
)

# 4. Update JS theme logic
content = content.replace(
    "else if (type === 'toolbtn') { editType = 'toolbtn'; name = 'Botones Herramienta'; }",
    "else if (type === 'toolbtn_discount') { editType = 'toolbtn_discount'; name = 'Botón Descuento'; }\n  else if (type === 'toolbtn_increase') { editType = 'toolbtn_increase'; name = 'Botón Aumento'; }\n  else if (type === 'toolbtn_vat') { editType = 'toolbtn_vat'; name = 'Botón IVA'; }"
)

content = content.replace(
    "} else if (type === 'toolbtn') {\n    currentCustomTheme.toolBtn = baseHex;",
    "} else if (type === 'toolbtn_discount') {\n    currentCustomTheme.toolBtnDiscount = baseHex;\n  } else if (type === 'toolbtn_increase') {\n    currentCustomTheme.toolBtnIncrease = baseHex;\n  } else if (type === 'toolbtn_vat') {\n    currentCustomTheme.toolBtnVat = baseHex;"
)

content = content.replace(
    "if (theme.toolBtn) root.style.setProperty('--calc-tool-btn', theme.toolBtn);\n  else root.style.removeProperty('--calc-tool-btn');",
    "if (theme.toolBtnDiscount) root.style.setProperty('--calc-tool-btn-discount', theme.toolBtnDiscount); else root.style.removeProperty('--calc-tool-btn-discount');\n  if (theme.toolBtnIncrease) root.style.setProperty('--calc-tool-btn-increase', theme.toolBtnIncrease); else root.style.removeProperty('--calc-tool-btn-increase');\n  if (theme.toolBtnVat) root.style.setProperty('--calc-tool-btn-vat', theme.toolBtnVat); else root.style.removeProperty('--calc-tool-btn-vat');"
)

# 5. Add custom themes logic and renderThemes function
custom_logic = """
function getCustomThemes() { try { return JSON.parse(localStorage.getItem('hogar_calc_custom_themes') || '[]'); } catch(e) { return []; } }
function setCustomThemes(themes) { localStorage.setItem('hogar_calc_custom_themes', JSON.stringify(themes)); }
function saveCustomTheme() {
  if (!currentCustomTheme) return;
  const name = prompt('Nombre para tu diseño:');
  if (!name) return;
  currentCustomTheme.name = name;
  const themes = getCustomThemes();
  themes.push(JSON.parse(JSON.stringify(currentCustomTheme)));
  setCustomThemes(themes);
  renderThemes();
  alert('Diseño "' + name + '" guardado correctamente.');
}
function deleteCustomTheme(index) {
  if(confirm('¿Estás seguro de que quieres borrar este diseño guardado?')) {
    const themes = getCustomThemes();
    themes.splice(index, 1);
    setCustomThemes(themes);
    renderThemes();
  }
}
function renderThemes() {
  const palette=document.getElementById('calculator-palette');
  if(!palette) return;
  let html = CALCULATOR_THEMES.map((theme,index)=>`<button class="calc-color" title="${theme.name}" style="background:linear-gradient(135deg,${theme.accent},${theme.display},${theme.opBottom})" onclick="setCalculatorTheme(CALCULATOR_THEMES[${index}]); toggleCalculatorPalette()"></button>`).join('');
  const custom = getCustomThemes();
  if (custom.length > 0) {
    html += '<div style="width:100%; height:1px; background:rgba(0,0,0,0.1); margin:4px 0;"></div>';
    html += custom.map((theme,index)=>`<div style="position:relative; display:inline-block;"><button class="calc-color" title="${theme.name}" style="background:linear-gradient(135deg,${theme.accent||'#ccc'},${theme.display||'#eee'},${theme.opBottom||'#ddd'})" onclick="setCalculatorTheme(getCustomThemes()[${index}]); toggleCalculatorPalette()"></button><button onclick="deleteCustomTheme(${index}); if(typeof event!=='undefined')event.stopPropagation();" style="position:absolute; top:-6px; right:-6px; background:white; border:1px solid #ccc; border-radius:50%; width:20px; height:20px; font-size:12px; display:flex; align-items:center; justify-content:center; cursor:pointer; color:red; box-shadow:0 2px 4px rgba(0,0,0,0.2); z-index:10;">✕</button></div>`).join('');
  }
  palette.innerHTML = html;
}
"""
content = content.replace(
    '// Init',
    custom_logic + '\n// Init'
)
content = content.replace(
    "if(palette)palette.innerHTML=CALCULATOR_THEMES.map((theme,index)=>`<button class=\"calc-color\" title=\"${theme.name}\" style=\"background:linear-gradient(135deg,${theme.accent},${theme.display},${theme.opBottom})\" onclick=\"setCalculatorTheme(CALCULATOR_THEMES[${index}]); toggleCalculatorPalette()\"></button>`).join('');",
    "renderThemes();"
)

# 6. Version and opacity
content = content.replace(
    '<div class="app-version" style="position:absolute; bottom:16px; right:16px; font-size:12px; font-weight:800; color:var(--calc-display-text); opacity:0.15; pointer-events:none;">v25</div>',
    '<div class="app-version" style="position:absolute; bottom:16px; right:16px; font-size:14px; font-weight:900; color:var(--calc-display-text); opacity:0.35; pointer-events:none;">v26</div>'
)

with open('index.html', 'w') as f:
    f.write(content)

