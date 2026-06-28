import re

with open('index.html', 'r') as f:
    content = f.read()

# Update handleEditModeSelect to pre-select color correctly with fallbacks
old_logic = """    let hex = '#ffffff';
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
    }"""

new_logic = """    let hex = '#ffffff';
    let defT = typeof CALCULATOR_THEMES !== 'undefined' ? CALCULATOR_THEMES[0] : {};
    if (currentCustomTheme) {
      if (editType === 'display') hex = currentCustomTheme.display || defT.display || hex;
      else if (editType === 'shell') hex = currentCustomTheme.shellTop || defT.shellTop || hex;
      else if (editType === 'toolpanel') hex = currentCustomTheme.toolPanel || currentCustomTheme.shellTop || defT.shellTop || hex;
      else if (editType === 'toolpanel_bg') hex = currentCustomTheme.toolPanelBg || '#ffffff';
      else if (editType === 'toolpanel_inputs') hex = currentCustomTheme.toolInputs || '#ffffff';
      else if (editType === 'toolpanel_calc_btn') hex = currentCustomTheme.toolCalcBtn || currentCustomTheme.accent || defT.accent || hex;
      else if (editType === 'toolbtn_discount') hex = currentCustomTheme.toolBtnDiscount || '#ffffff';
      else if (editType === 'toolbtn_increase') hex = currentCustomTheme.toolBtnIncrease || '#ffffff';
      else if (editType === 'toolbtn_vat') hex = currentCustomTheme.toolBtnVat || '#ffffff';
      else if (editType === 'easteregg') hex = currentCustomTheme.easterEgg || '#2ECC71';
      else if (editType.startsWith('key_')) {
         let k = editType.substring(4);
         if (currentCustomTheme.keys && currentCustomTheme.keys[k] && currentCustomTheme.keys[k].top) {
           hex = currentCustomTheme.keys[k].top;
         } else {
           let btn = document.querySelector(`[data-calc="${k}"]`);
           if (btn) {
              if (btn.classList.contains('op') || btn.classList.contains('calc-mini-key')) {
                 hex = currentCustomTheme.opTop || defT.opTop || hex;
              } else if (btn.classList.contains('top-op')) {
                 hex = currentCustomTheme.clearTop || defT.clearTop || hex;
              } else if (btn.classList.contains('equals')) {
                 hex = currentCustomTheme.accent || defT.accent || hex;
              } else if (btn.classList.contains('clear')) {
                 hex = currentCustomTheme.clearTop || defT.clearTop || hex;
              } else {
                 hex = currentCustomTheme.numTop || defT.numTop || hex;
              }
           }
         }
      }
    }"""

if old_logic in content:
    content = content.replace(old_logic, new_logic)
else:
    print("Failed to replace logic")

# Bump version to v52
content = content.replace('>v51</div>', '>v52</div>')

with open('index.html', 'w') as f:
    f.write(content)

