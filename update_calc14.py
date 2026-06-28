import re

with open('index.html', 'r') as f:
    content = f.read()

# 4. Modify handleCalcKey to support ACTIVE_TOOL_INPUT
js_key_search = """  if(/^\d$/.test(v)){CALC_CURRENT=CALC_CURRENT==='0'||CALC_JUST_EVALUATED?v:CALC_CURRENT+v;CALC_JUST_EVALUATED=false;}
  else if(v==='.'){if(CALC_JUST_EVALUATED)CALC_CURRENT='0';if(!CALC_CURRENT.includes('.'))CALC_CURRENT+='.';CALC_JUST_EVALUATED=false;}
  else if(v==='C'){CALC_CURRENT='0';CALC_PREVIOUS=null;CALC_OPERATOR='';CALC_JUST_EVALUATED=false;}
  else if(v==='back')CALC_CURRENT=CALC_CURRENT.length>1?CALC_CURRENT.slice(0,-1):'0';"""

js_key_replace = """  if(ACTIVE_TOOL_INPUT) {
    const el = document.getElementById(`calc-tool-${ACTIVE_TOOL_INPUT}`);
    if(el) {
      let val = el.value || '';
      if(v==='C') val = '';
      else if(v==='back') val = val.length > 1 ? val.slice(0,-1) : '';
      else if(/^\d$/.test(v)) val += v;
      else if(v==='.' || v===',') { if(!val.includes(',') && !val.includes('.')) val += ','; }
      el.value = val;
    }
    calcBeep();
    return;
  }
  if(/^\d$/.test(v)){CALC_CURRENT=CALC_CURRENT==='0'||CALC_JUST_EVALUATED?v:CALC_CURRENT+v;CALC_JUST_EVALUATED=false;}
  else if(v==='.' || v===','){if(CALC_JUST_EVALUATED)CALC_CURRENT='0';if(!CALC_CURRENT.includes('.'))CALC_CURRENT+='.';CALC_JUST_EVALUATED=false;}
  else if(v==='C'){CALC_CURRENT='0';CALC_PREVIOUS=null;CALC_OPERATOR='';CALC_JUST_EVALUATED=false;}
  else if(v==='back')CALC_CURRENT=CALC_CURRENT.length>1?CALC_CURRENT.slice(0,-1):'0';"""

if js_key_search in content:
    content = content.replace(js_key_search, js_key_replace)
else:
    print("WARNING: handleCalcKey logic not found")

with open('index.html', 'w') as f:
    f.write(content)
