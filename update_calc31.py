import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update .calc-key.equals CSS
old_equals_css = r".calc-key.equals\{background:linear-gradient\(180deg,color-mix\(in srgb,var\(--calc-accent\) 55%,#fff 45%\),var\(--calc-accent\)\);box-shadow:0 8px 0 var\(--calc-accent-dark\),0 11px 15px rgba\(0,0,0,\.26\),inset 0 2px 1px rgba\(255,255,255,\.95\)\}"
new_equals_css = ".calc-key.equals{background:linear-gradient(180deg,var(--calc-accent-top, color-mix(in srgb,var(--calc-accent) 55%,#fff 45%)),var(--calc-accent-bottom, var(--calc-accent)));box-shadow:0 8px 0 var(--calc-accent-dark),0 11px 15px rgba(0,0,0,.26),inset 0 2px 1px rgba(255,255,255,.95)}"
content = re.sub(old_equals_css, new_equals_css, content)

# 2. Update setCalculatorTheme to handle --calc-accent-top
old_set_equals = """         } else if (btn.classList.contains('equals')) {
           btn.style.setProperty('--calc-accent', colors.top);
           btn.style.setProperty('--calc-accent-dark', colors.shadow);"""
new_set_equals = """         } else if (btn.classList.contains('equals')) {
           btn.style.setProperty('--calc-accent-top', colors.top);
           btn.style.setProperty('--calc-accent-bottom', colors.bottom);
           btn.style.setProperty('--calc-accent-dark', colors.shadow);"""
content = content.replace(old_set_equals, new_set_equals)

# 3. We need a helper to compute the mix color in JS so the picker starts at the exact top color!
# If currentCustomTheme doesn't have an explicit color for '=', we fall back to mixing accent and white!
old_hex_equals = """} else if (btn.classList.contains('equals')) {
                 hex = currentCustomTheme.accent || defT.accent || hex;"""
new_hex_equals = """} else if (btn.classList.contains('equals')) {
                 let baseAccent = currentCustomTheme.accent || defT.accent || hex;
                 // Compute a 55% mix of baseAccent and 45% white to match CSS color-mix exactly
                 hex = mixHexWithWhite(baseAccent, 0.45);"""
content = content.replace(old_hex_equals, new_hex_equals)

# Add mixHexWithWhite helper
helper_fn = """function adjustBrightness(hex, percent) {
  let c = hexToRgb(hex);
  if (!c) return hex;
  let r = Math.max(0, Math.min(255, Math.round(c.r * percent)));
  let g = Math.max(0, Math.min(255, Math.round(c.g * percent)));
  let b = Math.max(0, Math.min(255, Math.round(c.b * percent)));
  return rgbToHex(r, g, b);
}

function mixHexWithWhite(hex, whiteRatio) {
  let c = hexToRgb(hex);
  if (!c) return hex;
  let r = Math.round(c.r * (1 - whiteRatio) + 255 * whiteRatio);
  let g = Math.round(c.g * (1 - whiteRatio) + 255 * whiteRatio);
  let b = Math.round(c.b * (1 - whiteRatio) + 255 * whiteRatio);
  return rgbToHex(r, g, b);
}"""

content = content.replace("""function adjustBrightness(hex, percent) {
  let c = hexToRgb(hex);
  if (!c) return hex;
  let r = Math.max(0, Math.min(255, Math.round(c.r * percent)));
  let g = Math.max(0, Math.min(255, Math.round(c.g * percent)));
  let b = Math.max(0, Math.min(255, Math.round(c.b * percent)));
  return rgbToHex(r, g, b);
}""", helper_fn)

# Bump version to v54
content = content.replace('>v53</div>', '>v54</div>')

with open('index.html', 'w') as f:
    f.write(content)

