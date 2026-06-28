import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update edit-top-bar to add delete button
content = content.replace(
    '<button onclick="saveCustomTheme()" style="background:#fff; color:#4A90E2; border:none; padding:8px 12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">💾 Guardar</button>',
    '<button onclick="deleteCurrentCustomTheme()" style="background:#ff4d4d; color:white; border:none; padding:8px 12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">🗑️ Borrar</button><button onclick="saveCustomTheme()" style="background:#fff; color:#4A90E2; border:none; padding:8px 12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">💾 Guardar</button>'
)

# 2. Add IDs to custom themes when saving/loading to track them
old_logic = """function getCustomThemes() { try { return JSON.parse(localStorage.getItem('hogar_calc_custom_themes') || '[]'); } catch(e) { return []; } }
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
}"""

custom_logic = """function getCustomThemes() { try { return JSON.parse(localStorage.getItem('hogar_calc_custom_themes') || '[]'); } catch(e) { return []; } }
function setCustomThemes(themes) { localStorage.setItem('hogar_calc_custom_themes', JSON.stringify(themes)); }
function saveCustomTheme() {
  if (!currentCustomTheme) return;
  const themes = getCustomThemes();
  if (currentCustomTheme.id) {
    if (confirm('¿Deseas ACTUALIZAR el diseño existente? (Pulsa Cancelar para guardarlo como una copia nueva)')) {
      const idx = themes.findIndex(t => t.id === currentCustomTheme.id);
      if (idx !== -1) {
        themes[idx] = JSON.parse(JSON.stringify(currentCustomTheme));
        setCustomThemes(themes);
        renderThemes();
        alert('Diseño actualizado correctamente.');
        return;
      }
    } else {
      delete currentCustomTheme.id;
    }
  }
  const name = prompt('Nombre para tu diseño:');
  if (!name) return;
  currentCustomTheme.name = name;
  currentCustomTheme.id = Date.now().toString();
  themes.push(JSON.parse(JSON.stringify(currentCustomTheme)));
  setCustomThemes(themes);
  renderThemes();
  alert('Diseño "' + name + '" guardado correctamente.');
}
function deleteCurrentCustomTheme() {
  if (!currentCustomTheme || !currentCustomTheme.id) {
    alert('Este diseño aún no está guardado, no se puede borrar.');
    return;
  }
  if(confirm('¿Estás seguro de que quieres borrar este diseño guardado?')) {
    const themes = getCustomThemes();
    const idx = themes.findIndex(t => t.id === currentCustomTheme.id);
    if (idx !== -1) {
      themes.splice(idx, 1);
      setCustomThemes(themes);
      renderThemes();
      toggleEditMode();
    }
  }
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
}"""

if old_logic in content:
    content = content.replace(old_logic, custom_logic)
else:
    print("Warning: old logic not found exactly")

# 3. Update CSS for inputs and calculate button
content = content.replace(
    '.calc-tool-field input{width:100%;min-height:42px;padding:8px 10px;border:1.5px solid rgba(52,35,28,.28);border-radius:9px;background:rgba(255,255,255,.82);color:#151515;font-size:18px;text-align:right}',
    '.calc-tool-field input{width:100%;min-height:42px;padding:8px 10px;border:1.5px solid rgba(52,35,28,.28);border-radius:9px;background:var(--calc-tool-inputs, rgba(255,255,255,.82));color:#151515;font-size:18px;text-align:right; cursor:pointer}'
)
content = content.replace(
    '.calc-tool-calculate{width:100%;min-height:42px;margin-top:9px;border:1px solid rgba(255,255,255,.7);border-radius:10px;color:#151515;font-weight:600;background:linear-gradient(180deg,color-mix(in srgb,var(--calc-accent) 55%,#fff 45%),var(--calc-accent));box-shadow:0 4px 0 var(--calc-accent-dark),0 6px 8px rgba(0,0,0,.16);cursor:pointer}',
    '.calc-tool-calculate{position:relative;overflow:hidden;width:100%;min-height:42px;margin-top:9px;border:1px solid rgba(255,255,255,.7);border-radius:10px;color:#151515;font-weight:600;background:linear-gradient(180deg,var(--calc-tool-calc-top,color-mix(in srgb,var(--calc-tool-calc-btn,var(--calc-accent)) 55%,#fff 45%)),var(--calc-tool-calc-bottom,var(--calc-tool-calc-btn,var(--calc-accent))));box-shadow:0 8px 0 var(--calc-tool-calc-shadow,var(--calc-accent-dark)),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95);cursor:pointer;--calc-tool-calc-top:color-mix(in srgb,var(--calc-tool-calc-btn,var(--calc-accent)) 60%,#FFF);--calc-tool-calc-bottom:var(--calc-tool-calc-btn,var(--calc-accent));--calc-tool-calc-shadow:color-mix(in srgb,var(--calc-tool-calc-btn,var(--calc-accent-dark)) 50%,#000);}.calc-tool-calculate:active{transform:translateY(8px);box-shadow:0 0 0 var(--calc-tool-calc-shadow,var(--calc-accent-dark)),inset 0 3px 5px rgba(0,0,0,.2)}'
)

# 4. Update JS theme selection for inputs and calculate button
content = content.replace(
    "else if (type === 'toolpanel') { editType = 'toolpanel'; name = 'Caja Descuento'; }",
    "else if (type === 'toolpanel') { editType = 'toolpanel'; name = 'Fondo Panel Descuento'; }\n  else if (type === 'toolpanel_inputs') { editType = 'toolpanel_inputs'; name = 'Cajas de Texto'; }\n  else if (type === 'toolpanel_calc_btn') { editType = 'toolpanel_calc_btn'; name = 'Botón Calcular'; }"
)

content = content.replace(
    "} else if (type === 'toolpanel') {\n    currentCustomTheme.toolPanel = baseHex;",
    "} else if (type === 'toolpanel') {\n    currentCustomTheme.toolPanel = baseHex;\n  } else if (type === 'toolpanel_inputs') {\n    currentCustomTheme.toolInputs = baseHex;\n  } else if (type === 'toolpanel_calc_btn') {\n    currentCustomTheme.toolCalcBtn = baseHex;"
)

content = content.replace(
    "if (theme.toolPanel) root.style.setProperty('--calc-tool-panel', theme.toolPanel);\n  else root.style.removeProperty('--calc-tool-panel');",
    "if (theme.toolPanel) root.style.setProperty('--calc-tool-panel', theme.toolPanel);\n  else root.style.removeProperty('--calc-tool-panel');\n  if (theme.toolInputs) root.style.setProperty('--calc-tool-inputs', theme.toolInputs);\n  else root.style.removeProperty('--calc-tool-inputs');\n  if (theme.toolCalcBtn) root.style.setProperty('--calc-tool-calc-btn', theme.toolCalcBtn);\n  else root.style.removeProperty('--calc-tool-calc-btn');"
)

# 5. Update HTML for inputs and calculate button to support selection
content = content.replace(
    '<input type="number" id="calc-tool-amount" placeholder="Ej. 100" pattern="[0-9]*" inputmode="decimal">',
    '<input type="number" id="calc-tool-amount" placeholder="Ej. 100" pattern="[0-9]*" inputmode="decimal" onclick="if(typeof isEditMode!==\'undefined\' && isEditMode) { if(typeof event!==\'undefined\' && event) event.stopPropagation(); handleEditModeSelect(\'toolpanel_inputs\'); }">'
)
content = content.replace(
    '<input type="number" id="calc-tool-percent" placeholder="Ej. 21" pattern="[0-9]*" inputmode="decimal">',
    '<input type="number" id="calc-tool-percent" placeholder="Ej. 21" pattern="[0-9]*" inputmode="decimal" onclick="if(typeof isEditMode!==\'undefined\' && isEditMode) { if(typeof event!==\'undefined\' && event) event.stopPropagation(); handleEditModeSelect(\'toolpanel_inputs\'); }">'
)
content = content.replace(
    '<button class="calc-tool-calculate" onclick="calculateCalcPercentTool()">Calcular</button>',
    '<button class="calc-tool-calculate" onclick="if(typeof isEditMode!==\'undefined\' && isEditMode) { if(typeof event!==\'undefined\' && event) event.stopPropagation(); handleEditModeSelect(\'toolpanel_calc_btn\'); } else calculateCalcPercentTool()">Calcular</button>'
)

# 6. Update tool buttons to always toggle panel even in edit mode
content = content.replace(
    'handleEditModeSelect(\'toolbtn_discount\'); } else toggleCalcPercentTool(\'discount\')',
    'handleEditModeSelect(\'toolbtn_discount\'); } toggleCalcPercentTool(\'discount\')'
)
content = content.replace(
    'handleEditModeSelect(\'toolbtn_increase\'); } else toggleCalcPercentTool(\'increase\')',
    'handleEditModeSelect(\'toolbtn_increase\'); } toggleCalcPercentTool(\'increase\')'
)
content = content.replace(
    'handleEditModeSelect(\'toolbtn_vat\'); } else toggleCalcPercentTool(\'vat\')',
    'handleEditModeSelect(\'toolbtn_vat\'); } toggleCalcPercentTool(\'vat\')'
)

# 7. Bump version text to v28
content = content.replace('>v27</div>', '>v28</div>')

with open('index.html', 'w') as f:
    f.write(content)

