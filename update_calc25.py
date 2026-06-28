import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add Rename button to top bar
topbar_search = '<div style="display:flex; align-items:center; gap:12px;"><button onclick="deleteCurrentCustomTheme()"'
topbar_replace = '<div style="display:flex; align-items:center; gap:8px;"><button onclick="renameCurrentCustomTheme()" title="Renombrar diseño" style="background:#fff; color:#4A90E2; border:none; padding:8px 10px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">✏️</button><button onclick="deleteCurrentCustomTheme()"'
if topbar_search in content:
    content = content.replace(topbar_search, topbar_replace)

# 2. Update saveCustomTheme and add renameCurrentCustomTheme
js_search = """function saveCustomTheme() {
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
}
function deleteCurrentCustomTheme() {"""

js_replace = """function saveCustomTheme() {
  if (!currentCustomTheme) return;
  const themes = getCustomThemes();
  
  if (currentCustomTheme.id) {
    if (confirm('¿Quieres SOBREESCRIBIR el diseño actual ("' + currentCustomTheme.name + '")?\\n\\nPulsa Aceptar para sobreescribir.\\nPulsa Cancelar para crear uno NUEVO.')) {
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
  
  const name = prompt('Nombre para tu NUEVO diseño:', currentCustomTheme.name ? currentCustomTheme.name + ' (Copia)' : 'Mi Diseño');
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
      return;
    }
  }
  
  currentCustomTheme.name = name;
  currentCustomTheme.id = Date.now().toString();
  themes.push(JSON.parse(JSON.stringify(currentCustomTheme)));
  setCustomThemes(themes);
  renderThemes();
  alert('Diseño "' + name + '" guardado correctamente.');
}

function renameCurrentCustomTheme() {
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
}

function deleteCurrentCustomTheme() {"""

if js_search in content:
    content = content.replace(js_search, js_replace)

# Bump version to v46
content = content.replace('>v45</div>', '>v46</div>')

with open('index.html', 'w') as f:
    f.write(content)

