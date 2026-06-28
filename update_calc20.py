import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update handleCalcKey
js_search = """function handleCalcKey(v){
  if(v==='colors'){toggleCalculatorPalette();return;}
  if (typeof isEditMode!=='undefined' && isEditMode) { handleEditModeSelect('key', v); return; }
  if(v==='sound'){toggleCalculatorSound();return;}
  calcBeep();
  if(v==='copy'){toggleCopyMenu();return;}"""

js_replace = """function handleCalcKey(v){
  if (typeof isEditMode!=='undefined' && isEditMode) { handleEditModeSelect('key', v); return; }
  if(v==='colors'){toggleCalculatorPalette();return;}
  if(v==='sound'){toggleCalculatorSound();return;}
  if(v==='elibi'){showEasterEgg();return;}
  calcBeep();
  if(v==='copy'){toggleCopyMenu();return;}"""
if js_search in content:
    content = content.replace(js_search, js_replace)

# 2. Update EliBi button HTML
elibi_search = '<button class="calc-mini-key calculator-signature-btn" onclick="showEasterEgg()"><img class="calculator-signature" src="logo_elibi.jpg" alt="EliBi"></button>'
elibi_replace = '<button class="calc-mini-key calculator-signature-btn" data-calc="elibi"><img class="calculator-signature" src="logo_elibi.jpg" alt="EliBi"></button>'
if elibi_search in content:
    content = content.replace(elibi_search, elibi_replace)

# 3. Update setCalculatorTheme for individual keys
theme_search = """  if (theme.keys) {
    for (let key in theme.keys) {
      let btn = document.querySelector(`.calc-key[data-calc="${key}"]`);
      if (btn) {
         let colors = theme.keys[key];
         if (btn.classList.contains('num')) {
           btn.style.setProperty('--calc-num-top', colors.top);
           btn.style.setProperty('--calc-num-bottom', colors.bottom);
           btn.style.setProperty('--calc-num-shadow', colors.shadow);
         } else if (btn.classList.contains('op')) {"""

theme_replace = """  if (theme.keys) {
    for (let key in theme.keys) {
      let btn = document.querySelector(`[data-calc="${key}"]`);
      if (btn) {
         let colors = theme.keys[key];
         if (btn.classList.contains('op') || btn.classList.contains('calc-mini-key')) {
           btn.style.setProperty('--calc-op-top', colors.top);
           btn.style.setProperty('--calc-op-bottom', colors.bottom);
           btn.style.setProperty('--calc-op-shadow', colors.shadow);
         } else if (btn.classList.contains('clear')) {"""
if theme_search in content:
    content = content.replace(theme_search, theme_replace)

# 4. Add fallback for num keys in setCalculatorTheme
theme_end_search = """         } else if (btn.classList.contains('equals')) {
           btn.style.setProperty('--calc-accent', colors.top);
           btn.style.setProperty('--calc-accent-dark', colors.shadow);
         }
      }
    }
  }"""
theme_end_replace = """         } else if (btn.classList.contains('equals')) {
           btn.style.setProperty('--calc-accent', colors.top);
           btn.style.setProperty('--calc-accent-dark', colors.shadow);
         } else {
           btn.style.setProperty('--calc-num-top', colors.top);
           btn.style.setProperty('--calc-num-bottom', colors.bottom);
           btn.style.setProperty('--calc-num-shadow', colors.shadow);
         }
      }
    }
  }"""
if theme_end_search in content:
    content = content.replace(theme_end_search, theme_end_replace)

# 5. Add edit-mode highlight for calc-mini-key
css_edit_search = 'body.edit-mode .calc-key::after, body.edit-mode .calculator-display::after, body.edit-mode .calc-tool-panel::after, body.edit-mode .calc-tool-button::after, body.edit-mode #easter-egg-text::after {'
css_edit_replace = 'body.edit-mode .calc-key::after, body.edit-mode .calc-mini-key::after, body.edit-mode .calculator-display::after, body.edit-mode .calc-tool-panel::after, body.edit-mode .calc-tool-button::after, body.edit-mode #easter-egg-text::after {'
if css_edit_search in content:
    content = content.replace(css_edit_search, css_edit_replace)

css_edit_active_search = 'body.edit-mode .calc-key:active::after, body.edit-mode .calculator-display:active::after, body.edit-mode .calc-tool-panel:active::after, body.edit-mode .calc-tool-button:active::after, body.edit-mode #easter-egg-text:active::after { opacity:1; }'
css_edit_active_replace = 'body.edit-mode .calc-key:active::after, body.edit-mode .calc-mini-key:active::after, body.edit-mode .calculator-display:active::after, body.edit-mode .calc-tool-panel:active::after, body.edit-mode .calc-tool-button:active::after, body.edit-mode #easter-egg-text:active::after { opacity:1; }'
if css_edit_active_search in content:
    content = content.replace(css_edit_active_search, css_edit_active_replace)

# 6. Add calc-mini-key reset to setCalculatorTheme
reset_search = """  document.querySelectorAll('.calc-key').forEach(btn => {
    btn.style.removeProperty('--calc-num-top');"""
reset_replace = """  document.querySelectorAll('.calc-key, .calc-mini-key').forEach(btn => {
    btn.style.removeProperty('--calc-num-top');"""
if reset_search in content:
    content = content.replace(reset_search, reset_replace)

# Bump version to v41
content = content.replace('>v40</div>', '>v41</div>')

with open('index.html', 'w') as f:
    f.write(content)

