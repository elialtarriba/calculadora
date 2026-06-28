import re

with open('index.html', 'r') as f:
    content = f.read()

# Update handleEditModeSelect to pre-select color
old_logic = """  if (editType) {
    currentEditType = editType;
    document.getElementById('edit-mode-target').innerText = name;
  }"""

new_logic = """  if (editType) {
    currentEditType = editType;
    document.getElementById('edit-mode-target').innerText = name;
    
    let hex = '#ffffff';
    if (currentCustomTheme) {
      if (editType === 'display' && currentCustomTheme.display) hex = currentCustomTheme.display;
      else if (editType === 'shell' && currentCustomTheme.shellTop) hex = currentCustomTheme.shellTop;
      else if (editType === 'toolpanel' && currentCustomTheme.toolPanel) hex = currentCustomTheme.toolPanel;
      else if (editType === 'toolpanel_bg' && currentCustomTheme.toolPanelBg) hex = currentCustomTheme.toolPanelBg;
      else if (editType === 'toolpanel_inputs' && currentCustomTheme.toolInputs) hex = currentCustomTheme.toolInputs;
      else if (editType === 'toolpanel_calc_btn' && currentCustomTheme.toolCalcBtn) hex = currentCustomTheme.toolCalcBtn;
      else if (editType === 'toolbtn_discount' && currentCustomTheme.toolBtnDiscount) hex = currentCustomTheme.toolBtnDiscount;
      else if (editType === 'toolbtn_increase' && currentCustomTheme.toolBtnIncrease) hex = currentCustomTheme.toolBtnIncrease;
      else if (editType === 'toolbtn_vat' && currentCustomTheme.toolBtnVat) hex = currentCustomTheme.toolBtnVat;
      else if (editType === 'easteregg' && currentCustomTheme.easterEgg) hex = currentCustomTheme.easterEgg;
      else if (editType.startsWith('key_') && currentCustomTheme.keys) {
         let k = editType.substring(4);
         if (currentCustomTheme.keys[k] && currentCustomTheme.keys[k].top) {
           hex = currentCustomTheme.keys[k].top;
         }
      }
    }
    
    if (/^#[0-9A-F]{6}$/i.test(hex)) {
      document.getElementById('edit-color-picker').value = hex;
    } else {
      document.getElementById('edit-color-picker').value = '#ffffff';
    }
  }"""

if old_logic in content:
    content = content.replace(old_logic, new_logic)
else:
    print("Failed to replace logic")

# Bump version to v49
content = content.replace('>v48</div>', '>v49</div>')

with open('index.html', 'w') as f:
    f.write(content)

