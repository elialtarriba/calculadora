import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update renameCurrentCustomTheme
rename_search = """function renameCurrentCustomTheme() {
  if (!currentCustomTheme || !currentCustomTheme.id) {
    alert('Guarda este diseño primero antes de poder renombrarlo.');
    return;
  }
  const themes = getCustomThemes();
  const idx = themes.findIndex(t => t.id === currentCustomTheme.id);
  if (idx === -1) return;
  const newName = prompt('Nuevo nombre para tu diseño:', currentCustomTheme.name);
  if (!newName || newName === currentCustomTheme.name) return;
  
  if (themes.some(t => t.name === newName)) {
     alert('Ya existe un diseño con ese nombre.');
     return;
  }
  
  currentCustomTheme.name = newName;
  themes[idx].name = newName;
  setCustomThemes(themes);
  renderThemes();
  document.getElementById('edit-mode-target').innerText = 'Fondo';
  alert('Diseño renombrado a: ' + newName);
}"""

rename_replace = """function renameCurrentCustomTheme() {
  if (!currentCustomTheme) return;
  const newName = prompt('Nombre para tu diseño:', currentCustomTheme.name || 'Mi Diseño');
  if (!newName || newName === currentCustomTheme.name) return;
  
  const themes = getCustomThemes();
  if (themes.some(t => t.name === newName)) {
     alert('Ya existe un diseño con ese nombre.');
     return;
  }
  
  currentCustomTheme.name = newName;
  if (currentCustomTheme.id) {
     const idx = themes.findIndex(t => t.id === currentCustomTheme.id);
     if (idx !== -1) {
        themes[idx].name = newName;
        setCustomThemes(themes);
        renderThemes();
     }
  }
  
  // Show the new name in the edit bar immediately
  document.getElementById('edit-mode-target').innerText = newName;
  
  if (currentCustomTheme.id) {
      alert('Diseño renombrado a: ' + newName);
  } else {
      alert('Nombre establecido. Recuerda Guardar para no perder los cambios.');
  }
}"""
if rename_search in content:
    content = content.replace(rename_search, rename_replace)


# 2. Add Colors Edit Modal HTML
modal_html = """<div id="colors-edit-modal" style="display:none; position:fixed; inset:0; background:rgba(0,0,0,0.5); z-index:1000; align-items:center; justify-content:center;">
  <div style="background:white; padding:20px; border-radius:16px; width:80%; max-width:320px; box-shadow:0 10px 25px rgba(0,0,0,0.2);">
    <button onclick="handleColorsEditModal(1)" style="width:100%; padding:14px; margin-bottom:10px; background:#f0f0f0; border:none; border-radius:10px; font-weight:bold; font-size:15px; color:#151515; cursor:pointer;">1. Cambiar color del botón Temas</button>
    <button onclick="handleColorsEditModal(2)" style="width:100%; padding:14px; margin-bottom:16px; background:#f0f0f0; border:none; border-radius:10px; font-weight:bold; font-size:15px; color:#151515; cursor:pointer;">2. Abrir Temas</button>
    <button onclick="handleColorsEditModal(0)" style="width:100%; padding:14px; background:#ff4d4d; color:white; border:none; border-radius:10px; font-weight:bold; font-size:15px; cursor:pointer;">Cancelar</button>
  </div>
</div>"""

if 'id="colors-edit-modal"' not in content:
    content = content.replace('<div class="calc-colors-overlay"', modal_html + '\n  <div class="calc-colors-overlay"')

# 3. Update Colors Edit Modal JS Logic
hk_search = """  if (v === 'colors' && typeof isEditMode !== 'undefined' && isEditMode) {
     if(confirm('¿Quieres CAMBIAR EL COLOR de este botón? (Pulsa Aceptar para darle color, o Cancelar para ABRIR LA PALETA DE TEMAS)')) {
       handleEditModeSelect('key', v);
     } else {
       toggleCalculatorPalette();
     }
     return;
  }"""
hk_replace = """  if (v === 'colors' && typeof isEditMode !== 'undefined' && isEditMode) {
     document.getElementById('colors-edit-modal').style.display = 'flex';
     return;
  }"""
if hk_search in content:
    content = content.replace(hk_search, hk_replace)

modal_js = """function handleColorsEditModal(action) {
  document.getElementById('colors-edit-modal').style.display = 'none';
  if (action === 1) {
    handleEditModeSelect('key', 'colors');
  } else if (action === 2) {
    toggleCalculatorPalette();
  }
}
"""
if 'function handleColorsEditModal' not in content:
    content = content.replace('function handleCalcKey', modal_js + 'function handleCalcKey')


# 4. Add editable background to expanded tool panel
css_search = ".calc-tool-panel{display:none;margin-top:10px;padding:12px;border:1px solid rgba(52,35,28,.18);border-radius:12px;background:rgba(255,255,255,.42)}"
css_replace = ".calc-tool-panel{display:none;margin-top:10px;padding:12px;border:1px solid rgba(52,35,28,.18);border-radius:12px;background:var(--calc-percent-panel-bg, rgba(255,255,255,.42))}"
if css_search in content:
    content = content.replace(css_search, css_replace)

html_search = '<div class="calc-tool-panel" id="calc-percent-panel">'
html_replace = '<div class="calc-tool-panel" id="calc-percent-panel" onclick="if(typeof isEditMode!==\\'undefined\\' && isEditMode) { if(typeof event!==\\'undefined\\' && event) event.stopPropagation(); handleEditModeSelect(\\'toolpanel_bg\\'); }">'
if html_search in content:
    content = content.replace(html_search, html_replace)

edit_sel_search = "else if (type === 'toolpanel') { editType = 'toolpanel'; name = 'Panel Herramientas'; }"
edit_sel_replace = "else if (type === 'toolpanel') { editType = 'toolpanel'; name = 'Panel Herramientas'; }\n  else if (type === 'toolpanel_bg') { editType = 'toolpanel_bg'; name = 'Fondo Caja Herramientas'; }"
if edit_sel_search in content:
    content = content.replace(edit_sel_search, edit_sel_replace)

color_app_search = "} else if (type === 'toolpanel') {"
color_app_replace = "} else if (type === 'toolpanel_bg') { currentCustomTheme.toolPanelBg = baseHex; } else if (type === 'toolpanel') {"
if color_app_search in content:
    content = content.replace(color_app_search, color_app_replace)

set_theme_search = "if (theme.toolPanel) root.style.setProperty('--calc-tool-panel', theme.toolPanel);"
set_theme_replace = "if (theme.toolPanel) root.style.setProperty('--calc-tool-panel', theme.toolPanel);\n  if (theme.toolPanelBg) root.style.setProperty('--calc-percent-panel-bg', theme.toolPanelBg); else root.style.removeProperty('--calc-percent-panel-bg');"
if set_theme_search in content:
    content = content.replace(set_theme_search, set_theme_replace)


# Bump version to v48
content = content.replace('>v47</div>', '>v48</div>')

with open('index.html', 'w') as f:
    f.write(content)

