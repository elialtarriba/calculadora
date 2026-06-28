import re

with open('index.html', 'r') as f:
    content = f.read()

# Update calculateCalcPercentTool logic
js_search = """function calculateCalcPercentTool(){
  const amount=calcToolNumber(document.getElementById('calc-tool-amount')?.value),percent=calcToolNumber(document.getElementById('calc-tool-percent')?.value),result=document.getElementById('calc-tool-result');
  if(!result||!CALC_PERCENT_TOOL)return;if(!Number.isFinite(amount)||!Number.isFinite(percent)||amount<0||percent<0){result.textContent='Introduce un importe y un porcentaje válidos.';return;}calcBeep();
  if(CALC_PERCENT_TOOL==='discount'){const removed=amount*percent/100;result.innerHTML=`<strong>Resultado: ${calcMoney(amount-removed)} €</strong><br>Se quitan ${calcMoney(removed)} € (${formatCalcValue(percent)} %).`;return;}
  if(CALC_PERCENT_TOOL==='increase'){const added=amount*percent/100;result.innerHTML=`<strong>Resultado: ${calcMoney(amount+added)} €</strong><br>Se suman ${calcMoney(added)} € (${formatCalcValue(percent)} %).`;return;}
  const net=amount/(1+percent/100);result.innerHTML=`<strong>Sin IVA: ${calcMoney(net)} €</strong><br>IVA incluido: ${calcMoney(amount-net)} € (${formatCalcValue(percent)} %).`;
}"""

js_replace = """function calculateCalcPercentTool(){
  const amount=calcToolNumber(document.getElementById('calc-tool-amount')?.value),percent=calcToolNumber(document.getElementById('calc-tool-percent')?.value),result=document.getElementById('calc-tool-result');
  if(!result||!CALC_PERCENT_TOOL)return;if(!Number.isFinite(amount)||!Number.isFinite(percent)||amount<0||percent<0){result.textContent='Introduce un importe y un porcentaje válidos.';return;}calcBeep();
  let finalAmount = 0; let explanation = ''; let historyExpr = '';
  if(CALC_PERCENT_TOOL==='discount'){
    const removed=amount*percent/100; finalAmount=amount-removed;
    explanation=`Se han quitado ${calcMoney(removed)} € (${formatCalcValue(percent)} %).`;
    historyExpr = `${formatCalcValue(amount)} - ${formatCalcValue(percent)}%`;
  }
  else if(CALC_PERCENT_TOOL==='increase'){
    const added=amount*percent/100; finalAmount=amount+added;
    explanation=`Se han sumado ${calcMoney(added)} € (${formatCalcValue(percent)} %).`;
    historyExpr = `${formatCalcValue(amount)} + ${formatCalcValue(percent)}%`;
  }
  else {
    finalAmount=amount/(1+percent/100);
    explanation=`IVA incluido extraído: ${calcMoney(amount-finalAmount)} € (${formatCalcValue(percent)} %).`;
    historyExpr = `Sin IVA (${formatCalcValue(percent)}%) de ${formatCalcValue(amount)}`;
  }
  result.innerHTML = explanation;
  calcCurrentValue = String(finalAmount); calcPreviousValue = ''; calcOperator = null; calcNewNumber = true;
  updateCalc();
  if (typeof addToHistory === 'function') addToHistory(historyExpr, finalAmount);
}"""

if js_search in content:
    content = content.replace(js_search, js_replace)
else:
    print("WARNING: calc tool js not found")

with open('index.html', 'w') as f:
    f.write(content)

