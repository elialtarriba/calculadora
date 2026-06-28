import re

with open('index.html', 'r') as f:
    content = f.read()

# Update calculateCalcPercentTool logic with correct variables
js_search = """  result.innerHTML = explanation;
  calcCurrentValue = String(finalAmount); calcPreviousValue = ''; calcOperator = null; calcNewNumber = true;
  updateCalc();
  if (typeof addToHistory === 'function') addToHistory(historyExpr, finalAmount);
}"""

js_replace = """  result.innerHTML = explanation;
  CALC_CURRENT = String(finalAmount); CALC_PREVIOUS = null; CALC_OPERATOR = ''; CALC_JUST_EVALUATED = true;
  updateCalc();
  if (typeof saveToHistory === 'function') saveToHistory(historyExpr, '', '', calcMoney(finalAmount));
}"""

if js_search in content:
    content = content.replace(js_search, js_replace)
else:
    print("WARNING: calc tool js variables not found")

# Bump version text to v34
content = content.replace('>v33</div>', '>v34</div>')

with open('index.html', 'w') as f:
    f.write(content)

