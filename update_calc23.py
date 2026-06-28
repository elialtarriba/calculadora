import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update data-calc for top back button
top_back_search = '<button class="calc-mini-key" data-calc="back" title="Borrar último número">⌫</button>'
top_back_replace = '<button class="calc-mini-key" data-calc="back_top" title="Borrar último número">⌫</button>'
if top_back_search in content:
    content = content.replace(top_back_search, top_back_replace)

# 1b. Update handleCalcKey for back_top
back_search = "else if(v==='back')CALC_CURRENT=CALC_CURRENT.length>1?CALC_CURRENT.slice(0,-1):'0';"
back_replace = "else if(v==='back' || v==='back_top')CALC_CURRENT=CALC_CURRENT.length>1?CALC_CURRENT.slice(0,-1):'0';"
if back_search in content:
    content = content.replace(back_search, back_replace)
    
back2_search = "else if(v==='back') val = val.length > 1 ? val.slice(0,-1) : '';"
back2_replace = "else if(v==='back' || v==='back_top') val = val.length > 1 ? val.slice(0,-1) : '';"
if back2_search in content:
    content = content.replace(back2_search, back2_replace)


# 2. Update saveCustomTheme logic
save_search = """function saveCustomTheme() {
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
}"""

save_replace = """function saveCustomTheme() {
  if (!currentCustomTheme) return;
  const themes = getCustomThemes();
  const name = prompt('Nombre para tu diseño:', currentCustomTheme.name || 'Mi Diseño');
  if (!name) return;
  
  const existingIdx = themes.findIndex(t => t.name === name);
  if (existingIdx !== -1) {
    if (confirm(`Ya existe un diseño con el nombre "${name}". ¿Quieres SOBREESCRIBIRLO?`)) {
      currentCustomTheme.id = themes[existingIdx].id;
      currentCustomTheme.name = name;
      themes[existingIdx] = JSON.parse(JSON.stringify(currentCustomTheme));
      setCustomThemes(themes);
      renderThemes();
      alert('Diseño actualizado correctamente.');
      return;
    } else {
      return; // User cancelled overwrite
    }
  }
  
  // Save as new
  currentCustomTheme.name = name;
  currentCustomTheme.id = Date.now().toString();
  themes.push(JSON.parse(JSON.stringify(currentCustomTheme)));
  setCustomThemes(themes);
  renderThemes();
  alert('Diseño "' + name + '" guardado correctamente.');
}"""

if save_search in content:
    content = content.replace(save_search, save_replace)


# 3. Update handleCalcKey for colors button logic
hk_search = """function handleCalcKey(v){
  if (typeof isEditMode!=='undefined' && isEditMode) { handleEditModeSelect('key', v); return; }
  if(v==='colors'){toggleCalculatorPalette();return;}"""

hk_replace = """function handleCalcKey(v){
  if (v === 'colors' && typeof isEditMode !== 'undefined' && isEditMode) {
     if(confirm('¿Quieres CAMBIAR EL COLOR de este botón? (Pulsa Aceptar para darle color, o Cancelar para ABRIR LA PALETA DE TEMAS)')) {
       handleEditModeSelect('key', v);
     } else {
       toggleCalculatorPalette();
     }
     return;
  }
  if (typeof isEditMode!=='undefined' && isEditMode) { handleEditModeSelect('key', v); return; }
  if(v==='colors'){toggleCalculatorPalette();return;}"""
if hk_search in content:
    content = content.replace(hk_search, hk_replace)

# Bump version text to v44
content = content.replace('>v43</div>', '>v44</div>')

with open('index.html', 'w') as f:
    f.write(content)

