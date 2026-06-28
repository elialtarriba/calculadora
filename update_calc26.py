import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update edit-top-bar buttons
topbar_search = '<div style="display:flex; align-items:center; gap:8px;"><button onclick="renameCurrentCustomTheme()" title="Renombrar diseño" style="background:#fff; color:#4A90E2; border:none; padding:8px 10px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">✏️</button><button onclick="deleteCurrentCustomTheme()" style="background:#ff4d4d; color:white; border:none; padding:8px 12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">🗑️ Borrar</button><button onclick="saveCustomTheme()" style="background:#fff; color:#4A90E2; border:none; padding:8px 12px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">💾 Guardar</button><input type="color"'
topbar_replace = '<div style="display:flex; align-items:center; gap:6px;"><button onclick="deleteCurrentCustomTheme()" title="Borrar diseño" style="background:#ff4d4d; color:white; border:none; padding:8px 10px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">🗑️</button><button onclick="renameCurrentCustomTheme()" title="Renombrar diseño" style="background:#fff; color:#4A90E2; border:none; padding:8px 10px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">✏️</button><button onclick="saveAsNewTheme()" style="background:#fff; color:#4A90E2; border:none; padding:8px 8px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">➕ Nuevo</button><button onclick="saveCustomTheme()" style="background:#fff; color:#4A90E2; border:none; padding:8px 8px; border-radius:10px; font-weight:bold; cursor:pointer; font-size:14px; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">💾 Guardar</button><input type="color"'

if topbar_search in content:
    content = content.replace(topbar_search, topbar_replace)
else:
    print("Failed to replace edit-top-bar buttons")


# 2. Update saveCustomTheme and saveAsNewTheme logic
js_search = """function saveCustomTheme() {
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
}"""

js_replace = """function saveCustomTheme() {
  if (!currentCustomTheme) return;
  const themes = getCustomThemes();
  
  if (currentCustomTheme.id) {
    if (confirm('¿Estás seguro de que quieres SOBREESCRIBIR el diseño "' + currentCustomTheme.name + '"?')) {
      const idx = themes.findIndex(t => t.id === currentCustomTheme.id);
      if (idx !== -1) {
        themes[idx] = JSON.parse(JSON.stringify(currentCustomTheme));
        setCustomThemes(themes);
        renderThemes();
        alert('Diseño actualizado correctamente.');
        return;
      }
    }
  } else {
    saveAsNewTheme();
  }
}

function saveAsNewTheme() {
  if (!currentCustomTheme) return;
  const themes = getCustomThemes();
  
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
}"""

if js_search in content:
    content = content.replace(js_search, js_replace)
else:
    print("Failed to replace saveCustomTheme logic")

# Bump version to v47
content = content.replace('>v46</div>', '>v47</div>')

with open('index.html', 'w') as f:
    f.write(content)

