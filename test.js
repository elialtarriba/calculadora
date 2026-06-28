
// LocalStorage helpers
function lsGet(k){try{return localStorage.getItem(k)}catch(e){return null}}
function lsSet(k,v){try{localStorage.setItem(k,v)}catch(e){}}

const CALCULATOR_THEMES=[
  {name:'Marrón pastel',accent:'#D98463',dark:'#B96546',shellTop:'#F8F3EA',shellBottom:'#E5DED0',display:'#B8DDE6',displayText:'#10222B',numTop:'#F2F1EC',numBottom:'#C9C9BD',numShadow:'#7E8177',opTop:'#EFF4FA',opBottom:'#CAD2DD',opShadow:'#8490A0',clearTop:'#FFE9E5',clearBottom:'#F2C0B7',clearShadow:'#D28D80'},
  {name:'Rosa luminoso',accent:'#E7A1B3',dark:'#C8758A',shellTop:'#FFF3F7',shellBottom:'#F2DDE6',display:'#FFD7E5',displayText:'#4D2635',numTop:'#FFF8FA',numBottom:'#EFD9E1',numShadow:'#C7A9B4',opTop:'#F7ECFF',opBottom:'#D9C8F0',opShadow:'#A58BC3',clearTop:'#FFF1DD',clearBottom:'#F3C692',clearShadow:'#D59755'},
  {name:'Azul agua',accent:'#7CB9C8',dark:'#4E8794',shellTop:'#EFFBFC',shellBottom:'#D6ECF0',display:'#BDECF2',displayText:'#173942',numTop:'#F5FBFA',numBottom:'#D5E5E1',numShadow:'#8FA8A3',opTop:'#E7F2FF',opBottom:'#BFD5EA',opShadow:'#799AB6',clearTop:'#FFE1DF',clearBottom:'#F0B1AA',clearShadow:'#C77670'},
  {name:'Menta',accent:'#94D1B0',dark:'#5EA87E',shellTop:'#F1FFF7',shellBottom:'#DCEFE5',display:'#C9F2DC',displayText:'#153A27',numTop:'#FAFFF8',numBottom:'#DDEADC',numShadow:'#93A98F',opTop:'#EAF6F0',opBottom:'#BED9CA',opShadow:'#79A089',clearTop:'#FFE7CE',clearBottom:'#F1BF82',clearShadow:'#C88744'},
  {name:'Lavanda',accent:'#B8A7E8',dark:'#8974C9',shellTop:'#F7F3FF',shellBottom:'#E5DDF5',display:'#DED5FF',displayText:'#2E2450',numTop:'#FCFAFF',numBottom:'#DDD7E8',numShadow:'#9A91A8',opTop:'#EEF0FF',opBottom:'#CBD0EE',opShadow:'#858CBD',clearTop:'#FFE0EC',clearBottom:'#EFB0C9',clearShadow:'#C57696'},
  {name:'Limón claro',accent:'#F3D266',dark:'#C7A326',shellTop:'#FFFBEA',shellBottom:'#EEE4BA',display:'#FFF1A9',displayText:'#493D10',numTop:'#FFFDF2',numBottom:'#E8E1C9',numShadow:'#A89B78',opTop:'#EFF8DD',opBottom:'#D0E2A5',opShadow:'#91A35F',clearTop:'#FFDCD2',clearBottom:'#EEAA95',clearShadow:'#C97860'},
  {name:'Marrón oscuro',accent:'#76513E',dark:'#3F2A21',shellTop:'#5B4338',shellBottom:'#2E211C',display:'#C9B39F',displayText:'#251811',numTop:'#A9856F',numBottom:'#6D4E3E',numShadow:'#2B1C16',opTop:'#8A6B59',opBottom:'#563C30',opShadow:'#241711',clearTop:'#C78E72',clearBottom:'#8F5943',clearShadow:'#4A2A20'},
  {name:'Marrón claro',accent:'#C9966B',dark:'#946442',shellTop:'#FFF4E8',shellBottom:'#DEC4AA',display:'#F2D7BC',displayText:'#4A2E1F',numTop:'#FFF9F1',numBottom:'#D9BFA6',numShadow:'#9B785C',opTop:'#F3E3D2',opBottom:'#C9A98A',opShadow:'#87664D',clearTop:'#FFE1CF',clearBottom:'#DCA889',clearShadow:'#A36E50'},
  {name:'Blanco',accent:'#D8D8D8',dark:'#9B9B9B',shellTop:'#FFFFFF',shellBottom:'#EAEAEA',display:'#F7F7F7',displayText:'#181818',numTop:'#FFFFFF',numBottom:'#E8E8E8',numShadow:'#A6A6A6',opTop:'#F8F8F8',opBottom:'#DADADA',opShadow:'#999999',clearTop:'#FFFFFF',clearBottom:'#E3E3E3',clearShadow:'#A0A0A0'},
  {name:'Violeta',accent:'#9B59B6',dark:'#8E44AD',shellTop:'#F9F2FB',shellBottom:'#E5D5E8',display:'#F5EEF8',displayText:'#311B38',numTop:'#FFFFFF',numBottom:'#D8C8DB',numShadow:'#938297',opTop:'#F1E7F2',opBottom:'#CBB6CE',opShadow:'#87728A',clearTop:'#FFE1DF',clearBottom:'#F0B1AA',clearShadow:'#C77670'},
  {name:'Naranja',accent:'#F39C12',dark:'#E67E22',shellTop:'#FFF7EC',shellBottom:'#F5E1C8',display:'#FEF5E7',displayText:'#452A06',numTop:'#FFFFFF',numBottom:'#E3D1B9',numShadow:'#A1927F',opTop:'#FAEBDD',opBottom:'#D5C1AA',opShadow:'#948574',clearTop:'#FFDEE2',clearBottom:'#F2AAB4',clearShadow:'#C46E79'},
  {name:'Turquesa',accent:'#1ABC9C',dark:'#16A085',shellTop:'#E9F7F5',shellBottom:'#C9E8E1',display:'#E8F8F5',displayText:'#063A2E',numTop:'#F8FCFB',numBottom:'#BBD9D3',numShadow:'#7C9791',opTop:'#E0F0EC',opBottom:'#B1CBC5',opShadow:'#6E8580',clearTop:'#FFE3CD',clearBottom:'#F5BB90',clearShadow:'#CA8B5D'},
  {name:'Cereza',accent:'#E74C3C',dark:'#C0392B',shellTop:'#FDF0EF',shellBottom:'#F1CDCA',display:'#FDEDEC',displayText:'#380B07',numTop:'#FFFFFF',numBottom:'#DDBFBC',numShadow:'#9C817F',opTop:'#F6E5E3',opBottom:'#D4B8B6',opShadow:'#957B7A',clearTop:'#FDF2E2',clearBottom:'#EFD5AD',clearShadow:'#B9A07D'},
  {name:'Medianoche',accent:'#34495E',dark:'#2C3E50',shellTop:'#445362',shellBottom:'#1C2732',display:'#BDC3C7',displayText:'#10171D',numTop:'#A0AEB8',numBottom:'#596C7D',numShadow:'#182129',opTop:'#7B8996',opBottom:'#415161',opShadow:'#0D141B',clearTop:'#BAA79B',clearBottom:'#78675C',clearShadow:'#362C25'},
  {name:'Oro Rosa',accent:'#E5989B',dark:'#B5838D',shellTop:'#FFEDEB',shellBottom:'#E8D5D4',display:'#FFEDEB',displayText:'#4A3537',numTop:'#FFF9F8',numBottom:'#DBBFC2',numShadow:'#9E8387',opTop:'#F8EAE9',opBottom:'#D3BCBE',opShadow:'#917D80',clearTop:'#EAE7ED',clearBottom:'#A8A3B2',clearShadow:'#686373'},
  {name:'Lima',accent:'#B4D330',dark:'#94AE25',shellTop:'#FAFDED',shellBottom:'#E3ECBE',display:'#FAFDED',displayText:'#2E3807',numTop:'#FFFFFF',numBottom:'#D1DBAC',numShadow:'#8E996B',opTop:'#F0F6D5',opBottom:'#C9D3A0',opShadow:'#848F5D',clearTop:'#FEEAE5',clearBottom:'#F2BBAE',clearShadow:'#C1887B'},
  {name:'Cielo Nocturno',accent:'#2980B9',dark:'#2471A3',shellTop:'#EAF2F8',shellBottom:'#B3D0E5',display:'#EAF2F8',displayText:'#0B2135',numTop:'#F8FAFC',numBottom:'#A1B8CA',numShadow:'#60778C',opTop:'#D9E6F0',opBottom:'#9CAEC0',opShadow:'#5B6F82',clearTop:'#FEEAE5',clearBottom:'#F2BBAE',clearShadow:'#C1887B'},
  {name:'Frambuesa',accent:'#C71585',dark:'#9E106A',shellTop:'#FDF0F7',shellBottom:'#F1C2DF',display:'#FDF0F7',displayText:'#360423',numTop:'#FFFFFF',numBottom:'#DCACC8',numShadow:'#9D738A',opTop:'#F6DFED',opBottom:'#D5AED0',opShadow:'#977793',clearTop:'#FEEAE5',clearBottom:'#F2BBAE',clearShadow:'#C1887B'},
  {name:'Gris',accent:'#7F8C8D',dark:'#707B7C',shellTop:'#F2F4F4',shellBottom:'#D4D7D7',display:'#F2F4F4',displayText:'#1F2424',numTop:'#FFFFFF',numBottom:'#C2C7C7',numShadow:'#868E8E',opTop:'#E7EAEB',opBottom:'#B7BCBC',opShadow:'#7A8181',clearTop:'#FEEAE5',clearBottom:'#F2BBAE',clearShadow:'#C1887B'},
  {name:'Mandarina',accent:'#E67E22',dark:'#D35400',shellTop:'#FDEBD0',shellBottom:'#F5CBA7',display:'#FAE5D3',displayText:'#6E2C00',numTop:'#FEF9E7',numBottom:'#FAD7A1',numShadow:'#D68910',opTop:'#FADBD8',opBottom:'#E6B0AA',opShadow:'#A93226',clearTop:'#FDF2E9',clearBottom:'#EDBB99',clearShadow:'#BA4A00'},
  {name:'Otoño',accent:'#D35400',dark:'#A04000',shellTop:'#FCF3CF',shellBottom:'#F5B041',display:'#F9E79F',displayText:'#784212',numTop:'#FEF9E7',numBottom:'#F8C471',numShadow:'#B9770E',opTop:'#FDEBD0',opBottom:'#F5CBA7',opShadow:'#BA4A00',clearTop:'#FADBD8',clearBottom:'#E6B0AA',clearShadow:'#922B21'},
  {name:'Melocotón',accent:'#F5B041',dark:'#E67E22',shellTop:'#FDF2E9',shellBottom:'#FAE5D3',display:'#FDF2E9',displayText:'#512E05',numTop:'#FFFFFF',numBottom:'#F5D9C4',numShadow:'#CD9D7F',opTop:'#FADBD8',opBottom:'#E8AFA7',opShadow:'#B26458',clearTop:'#FCF3CF',clearBottom:'#F4D03F',clearShadow:'#C39F24',topOpTop:'#FADBD8',topOpBottom:'#E8AFA7',topOpShadow:'#B26458'},
  {name:'Pastel Sorpresa',accent:'#FFB347',dark:'#E69622',shellTop:'#F4F5F7',shellBottom:'#E0E4E8',display:'#FFF1E0',displayText:'#362C22',numTop:'#FFFFE0',numBottom:'#F8EEB2',numShadow:'#C9C289',opTop:'#EBECEF',opBottom:'#C9CED6',opShadow:'#919AA6',clearTop:'#DEDFE3',clearBottom:'#B0B6C2',clearShadow:'#7A8291',topOpTop:'#EBECEF',topOpBottom:'#C9CED6',topOpShadow:'#919AA6'}
];

let CALC_CURRENT='0', CALC_PREVIOUS=null, CALC_OPERATOR='', CALC_JUST_EVALUATED=false;
let CALC_SOUND=true, CALC_AUDIO=null;
let CALC_PERCENT_TOOL='';
document.addEventListener('visibilitychange', () => { if(document.visibilityState === 'hidden' && CALC_PERCENT_TOOL) toggleCalcPercentTool(CALC_PERCENT_TOOL); });
let ACTIVE_TOOL_INPUT=null;
let CALC_HISTORY = [];

function formatCalcValue(value){const n=Number(value);return Number.isFinite(n)?String(Math.round(n*100000000)/100000000).replace('.',','):'Error';}

let showingEasterEgg = false;
const easterEggQuotes = [
  "✨ ¡Tú puedes con todo! ✨", "🌟 ¡Hoy es un gran día! 🌟", "💫 ¡Sonríe, estás genial! 💫", 
  "✨ ¡Eres imparable! ✨", "🌟 ¡Confía en tu magia! 🌟", "✨ ¡Sigue brillando! ✨",
  "🌟 ¡No te rindas nunca! 🌟", "💫 ¡Cree en ti siempre! 💫", "✨ ¡Todo es posible! ✨",
  "🌟 ¡Haz que suceda! 🌟", "✨ ¡Atrévete a soñar! ✨", "💫 ¡Eres pura energía! 💫",
  "🌟 ¡Lo vas a lograr! 🌟", "✨ ¡Supera tus límites! ✨", "💫 ¡Disfruta el momento! 💫",
  "🌟 ¡Vuela muy alto! 🌟", "✨ ¡Magia en cada paso! ✨", "💫 ¡Eres luz y fuerza! 💫",
  "🌟 ¡Nunca dejes de reír! 🌟", "✨ ¡Celebra tus éxitos! ✨", "💫 ¡El éxito te espera! 💫",
  "🌟 ¡Siente tu poder! 🌟", "✨ ¡Eres inspiración! ✨", "💫 ¡Brilla con fuerza! 💫",
  "🌟 ¡Hazlo con pasión! 🌟", "✨ ¡Sigue tu corazón! ✨", "💫 ¡Despierta tu genio! 💫",
  "🌟 ¡Tu esfuerzo vale oro! 🌟", "✨ ¡Persigue tus metas! ✨", "💫 ¡Crea tu propio destino! 💫",
  "✨ ¡El límite es el cielo! ✨", "🌟 ¡Saca tu mejor versión! 🌟", "💫 ¡Toma las riendas! 💫",
  "✨ ¡Respira y confía! ✨", "🌟 ¡Hoy es tu momento! 🌟", "💫 ¡Deja huella! 💫",
  "✨ ¡Avanza sin miedo! ✨", "🌟 ¡Tu luz ilumina! 🌟", "💫 ¡Piensa en grande! 💫",
  "✨ ¡Sueña sin límites! ✨", "🌟 ¡Tus ideas valen! 🌟", "💫 ¡Actitud positiva! 💫",
  "✨ ¡Hazte escuchar! ✨", "🌟 ¡Rompe los moldes! 🌟", "💫 ¡Vales oro! 💫",
  "✨ ¡El futuro es tuyo! ✨", "🌟 ¡Paso a paso, siempre! 🌟", "💫 ¡Crea magia! 💫",
  "✨ ¡Tú eres la chispa! ✨", "🌟 ¡Sorprende al mundo! 🌟", "💫 ¡Sé tu propia musa! 💫",
  "✨ ¡Levántate y brilla! ✨", "🌟 ¡Escribe tu historia! 🌟", "💫 ¡No hay imposibles! 💫",
  "✨ ¡Vive tu aventura! ✨", "🌟 ¡Atrévete a ser tú! 🌟", "💫 ¡El éxito te abraza! 💫",
  "✨ ¡Fluye con la vida! ✨", "🌟 ¡Todo a tu favor! 🌟", "💫 ¡Imagina y crea! 💫"
];
function showEasterEgg() {
  showingEasterEgg = true;
  const quote = easterEggQuotes[Math.floor(Math.random() * easterEggQuotes.length)];
  document.getElementById('calc-expression').innerHTML = '';
  document.getElementById('calc-value').innerHTML = `<span id="easter-egg-text" onclick="if(typeof isEditMode!=='undefined' && isEditMode) { if(typeof event!=='undefined' && event) event.stopPropagation(); handleEditModeSelect('easteregg'); }" style="font-size:clamp(16px,5vw,26px);color:var(--calc-easter-egg, var(--calc-accent));font-weight:900;font-family:ui-rounded,'SF Pro Rounded',Arial,sans-serif;letter-spacing:0;text-align:center;display:block;padding:10px 0;position:relative;">${quote}</span>`;
}
function handleDisplayClick() {
  if (typeof isEditMode!=='undefined' && isEditMode) { handleEditModeSelect('display'); return; }
  if (showingEasterEgg) {
    showingEasterEgg = false;
    updateCalc();
  } else {
    toggleHistory();
  }
}

function updateCalc(){
  showingEasterEgg = false;
  const value=document.getElementById('calc-value'),expression=document.getElementById('calc-expression'),sound=document.getElementById('calc-sound');
  if(value)value.textContent=CALC_CURRENT.replace('.',',');
  if(expression)expression.textContent=CALC_PREVIOUS!==null&&CALC_OPERATOR?`${formatCalcValue(CALC_PREVIOUS)} ${CALC_OPERATOR.replace('*','×').replace('/','÷')}`:'';
  if(sound){sound.textContent=CALC_SOUND?'🔊':'🔇';sound.title=CALC_SOUND?'Desactivar sonido':'Activar sonido';}
}

function calculateCalcValues(){
  const a=Number(CALC_PREVIOUS),b=Number(CALC_CURRENT);let result=b;
  let opSymbol = CALC_OPERATOR;
  if(CALC_OPERATOR==='+')result=a+b;if(CALC_OPERATOR==='-')result=a-b;
  if(CALC_OPERATOR==='*'){result=a*b; opSymbol = '×';}
  if(CALC_OPERATOR==='/'){result=b===0?NaN:a/b; opSymbol = '÷';}
  
  // Save to history
  if (CALC_PREVIOUS !== null && CALC_OPERATOR) {
    saveToHistory(formatCalcValue(a), opSymbol, formatCalcValue(b), formatCalcValue(result));
  }
  
  CALC_CURRENT=formatCalcValue(result).replace(',','.');CALC_PREVIOUS=null;CALC_OPERATOR='';CALC_JUST_EVALUATED=true;
}

function saveToHistory(a, op, b, res) {
  const date = new Date().toLocaleDateString('es-ES', {day: 'numeric', month: 'short', hour:'2-digit', minute:'2-digit'}).toUpperCase();
  CALC_HISTORY.unshift({ a, op, b, res, date });
  if (CALC_HISTORY.length > 50) CALC_HISTORY.pop();
  lsSet('hogar_calc_history', JSON.stringify(CALC_HISTORY));
  renderHistory();
}

function loadHistory() {
  try {
    CALC_HISTORY = JSON.parse(lsGet('hogar_calc_history')) || [];
  } catch(e) { CALC_HISTORY = []; }
  renderHistory();
}

function renderHistory() {
  const list = document.getElementById('calc-history-list');
  if (!list) return;
  if (CALC_HISTORY.length === 0) {
    list.innerHTML = '<div style="text-align:center; padding: 20px; color:rgba(0,0,0,0.4); font-weight:800; font-size:14px;">No hay operaciones guardadas</div>';
    return;
  }
  list.innerHTML = CALC_HISTORY.map(h => `
    <div class="calc-history-item">
      <div class="hist-date">${h.date}</div>
      <div class="hist-icon">💬</div>
      <div class="hist-expr">${h.a} ${h.op} ${h.b}</div>
      <div>= ${h.res}</div>
    </div>
  `).join('');
}

function toggleHistory() {
  const ov = document.getElementById('calc-history-overlay');
  ov.classList.toggle('open');
}

function clearHistory() {
  CALC_HISTORY = [];
  lsSet('hogar_calc_history', '[]');
  renderHistory();
  toggleHistory();
}

function calcBeep(){
  if(!CALC_SOUND)return;
  try{
    const Ctx=window.AudioContext||window.webkitAudioContext;
    CALC_AUDIO=CALC_AUDIO||new Ctx();
    const osc=CALC_AUDIO.createOscillator(),gain=CALC_AUDIO.createGain(),now=CALC_AUDIO.currentTime;
    osc.type='sine';osc.frequency.setValueAtTime(520,now);osc.frequency.exponentialRampToValueAtTime(230,now+.045);
    gain.gain.setValueAtTime(.035,now);gain.gain.exponentialRampToValueAtTime(.001,now+.05);
    osc.connect(gain);gain.connect(CALC_AUDIO.destination);
    osc.start(now);osc.stop(now+.055);
  }catch(e){}
}
function toggleCalculatorSound(){CALC_SOUND=!CALC_SOUND;lsSet('hogar_calc_sound',CALC_SOUND?'1':'0');updateCalc();calcBeep();}

function handleColorsEditModal(action) {
  document.getElementById('colors-edit-modal').style.display = 'none';
  if (action === 1) {
    handleEditModeSelect('key', 'colors');
  } else if (action === 2) {
    toggleCalculatorPalette();
  }
}
function handleCalcKey(v){
  if (v === 'colors' && typeof isEditMode !== 'undefined' && isEditMode) {
     document.getElementById('colors-edit-modal').style.display = 'flex';
     return;
  }
  if (typeof isEditMode!=='undefined' && isEditMode) { handleEditModeSelect('key', v); return; }
  if(v==='colors'){toggleCalculatorPalette();return;}
  if(v==='sound'){toggleCalculatorSound();return;}
  if(v==='elibi'){showEasterEgg();return;}
  calcBeep();
  if(v==='copy'){toggleCopyMenu();return;}
  if(ACTIVE_TOOL_INPUT) {
    const el = document.getElementById(`calc-tool-${ACTIVE_TOOL_INPUT}`);
    if(el) {
      let val = el.value || '';
      if(v==='C') val = '';
      else if(v==='back' || v==='back_top') val = val.length > 1 ? val.slice(0,-1) : '';
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
  else if(v==='back' || v==='back_top')CALC_CURRENT=CALC_CURRENT.length>1?CALC_CURRENT.slice(0,-1):'0';
  else if(v==='+/-')CALC_CURRENT=String((Number(CALC_CURRENT)||0)*-1);
  else if(v==='%'){const p=(Number(CALC_CURRENT)||0)/100;CALC_CURRENT=String(CALC_PREVIOUS!==null&&['+','-'].includes(CALC_OPERATOR)?Number(CALC_PREVIOUS)*p:p);}
  else if(['+','-','*','/'].includes(v)){if(CALC_PREVIOUS!==null&&CALC_OPERATOR&&!CALC_JUST_EVALUATED)calculateCalcValues();CALC_PREVIOUS=Number(CALC_CURRENT);CALC_OPERATOR=v;CALC_JUST_EVALUATED=true;}
  else if(v==='='&&CALC_PREVIOUS!==null&&CALC_OPERATOR)calculateCalcValues();
  updateCalc();
}

function toggleCalculatorPalette(){
  const p=document.getElementById('calc-colors-overlay');
  if(p){p.classList.toggle('open');}
}
function toggleCopyMenu() {
  document.getElementById('calc-copy-overlay').classList.toggle('open');
}
function executeCopy(suffix) {
  const num = CALC_CURRENT.replace('.', ',');
  navigator.clipboard?.writeText(num + suffix);
  toggleCopyMenu();
}
function setCalculatorTheme(theme){
  const root=document.getElementById('calculator-shell');if(!root||!theme)return;
  [['accent','--calc-accent'],['dark','--calc-accent-dark'],['shellTop','--calc-shell-top'],['shellBottom','--calc-shell-bottom'],['display','--calc-display'],['displayText','--calc-display-text'],['numTop','--calc-num-top'],['numBottom','--calc-num-bottom'],['numShadow','--calc-num-shadow'],['opTop','--calc-op-top'],['opBottom','--calc-op-bottom'],['opShadow','--calc-op-shadow'],['clearTop','--calc-clear-top'],['clearBottom','--calc-clear-bottom'],['clearShadow','--calc-clear-shadow']].forEach(([key,prop])=>{
    if(theme[key]) root.style.setProperty(prop,theme[key]);
    else root.style.removeProperty(prop);
  });
  if(theme.topOpTop){
    root.style.setProperty('--calc-top-op-top',theme.topOpTop);
    root.style.setProperty('--calc-top-op-bottom',theme.topOpBottom);
    root.style.setProperty('--calc-top-op-shadow',theme.topOpShadow);
  } else {
    root.style.setProperty('--calc-top-op-top',theme.clearTop);
    root.style.setProperty('--calc-top-op-bottom',theme.clearBottom);
    root.style.setProperty('--calc-top-op-shadow',theme.clearShadow);
  }

  if (theme.toolPanel) root.style.setProperty('--calc-tool-panel', theme.toolPanel);
  else root.style.removeProperty('--calc-tool-panel');
  if (theme.toolPanelBg) root.style.setProperty('--calc-percent-panel-bg', theme.toolPanelBg);
  else root.style.removeProperty('--calc-percent-panel-bg');
  if (theme.toolInputs) root.style.setProperty('--calc-tool-inputs', theme.toolInputs);
  else root.style.removeProperty('--calc-tool-inputs');
  if (theme.toolCalcBtn) root.style.setProperty('--calc-tool-calc-btn', theme.toolCalcBtn);
  else root.style.removeProperty('--calc-tool-calc-btn');

  if (theme.toolBtnDiscount) root.style.setProperty('--calc-tool-btn-discount', theme.toolBtnDiscount); else root.style.removeProperty('--calc-tool-btn-discount');
  if (theme.toolBtnIncrease) root.style.setProperty('--calc-tool-btn-increase', theme.toolBtnIncrease); else root.style.removeProperty('--calc-tool-btn-increase');
  if (theme.toolBtnVat) root.style.setProperty('--calc-tool-btn-vat', theme.toolBtnVat); else root.style.removeProperty('--calc-tool-btn-vat');

  if (theme.easterEgg) root.style.setProperty('--calc-easter-egg', theme.easterEgg);
  else root.style.removeProperty('--calc-easter-egg');

  document.querySelectorAll('.calc-key, .calc-mini-key').forEach(btn => {
    btn.style.removeProperty('--calc-num-top');
    btn.style.removeProperty('--calc-num-bottom');
    btn.style.removeProperty('--calc-num-shadow');
    btn.style.removeProperty('--calc-op-top');
    btn.style.removeProperty('--calc-op-bottom');
    btn.style.removeProperty('--calc-op-shadow');
    btn.style.removeProperty('--calc-clear-top');
    btn.style.removeProperty('--calc-clear-bottom');
    btn.style.removeProperty('--calc-clear-shadow');
    btn.style.removeProperty('--calc-top-op-top');
    btn.style.removeProperty('--calc-top-op-bottom');
    btn.style.removeProperty('--calc-top-op-shadow');
    btn.style.removeProperty('--calc-accent');
    btn.style.removeProperty('--calc-accent-dark');
  });

  if (theme.keys) {
    for (let key in theme.keys) {
      let btn = document.querySelector(`[data-calc="${key}"]`);
      if (btn) {
         let colors = theme.keys[key];
         if (btn.classList.contains('op') || btn.classList.contains('calc-mini-key')) {
           btn.style.setProperty('--calc-op-top', colors.top);
           btn.style.setProperty('--calc-op-bottom', colors.bottom);
           btn.style.setProperty('--calc-op-shadow', colors.shadow);
         } else if (btn.classList.contains('clear')) {
           btn.style.setProperty('--calc-clear-top', colors.top);
           btn.style.setProperty('--calc-clear-bottom', colors.bottom);
           btn.style.setProperty('--calc-clear-shadow', colors.shadow);
         } else if (btn.classList.contains('top-op')) {
           btn.style.setProperty('--calc-top-op-top', colors.top);
           btn.style.setProperty('--calc-top-op-bottom', colors.bottom);
           btn.style.setProperty('--calc-top-op-shadow', colors.shadow);
         } else if (btn.classList.contains('equals')) {
           btn.style.setProperty('--calc-accent-top', colors.top);
           btn.style.setProperty('--calc-accent-bottom', colors.bottom);
           btn.style.setProperty('--calc-accent-dark', colors.shadow);
         } else {
           btn.style.setProperty('--calc-num-top', colors.top);
           btn.style.setProperty('--calc-num-bottom', colors.bottom);
           btn.style.setProperty('--calc-num-shadow', colors.shadow);
         }
      }
    }
  }
  
  lsSet('hogar_calc_theme', JSON.stringify(theme));
  document.querySelector('meta[name="theme-color"]').setAttribute('content', theme.shellBottom);
}

function toggleCalcPercentTool(tool){
  const panel=document.getElementById('calc-percent-panel'),result=document.getElementById('calc-tool-result'),label=document.getElementById('calc-tool-percent-label');
  CALC_PERCENT_TOOL=panel.classList.contains('open')&&CALC_PERCENT_TOOL===tool?'':tool;panel.classList.toggle('open',Boolean(CALC_PERCENT_TOOL));
  ['discount','increase','vat'].forEach(k=>document.getElementById(`calc-${k}-button`)?.classList.toggle('active',CALC_PERCENT_TOOL===k));
  if(label)label.textContent=CALC_PERCENT_TOOL==='vat'?'IVA %':'Porcentaje %';
  if(result)result.textContent=CALC_PERCENT_TOOL==='vat'?'Escribe el precio con IVA y el porcentaje de IVA.':CALC_PERCENT_TOOL==='increase'?'Escribe el importe y el porcentaje que quieres sumar.':'Escribe el importe y el porcentaje que quieres quitar.';
  if(CALC_PERCENT_TOOL) setActiveToolInput('amount');
  else setActiveToolInput(null);
}
function setActiveToolInput(inputId) {
  ACTIVE_TOOL_INPUT = inputId;
  const amt = document.getElementById('calc-tool-amount');
  const pct = document.getElementById('calc-tool-percent');
  if(amt) amt.style.boxShadow = inputId === 'amount' ? '0 0 0 3px #4A90E2' : 'none';
  if(pct) pct.style.boxShadow = inputId === 'percent' ? '0 0 0 3px #4A90E2' : 'none';
}
function calcToolNumber(value){const n=Number(String(value||'').trim().replace(/\s/g,'').replace(',','.'));return Number.isFinite(n)?n:NaN;}
function calcMoney(value){return Number(value).toLocaleString('es-ES',{minimumFractionDigits:2,maximumFractionDigits:2});}
function calculateCalcPercentTool(){
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
  CALC_CURRENT = String(finalAmount); CALC_PREVIOUS = null; CALC_OPERATOR = ''; CALC_JUST_EVALUATED = true;
  updateCalc();
  if (typeof saveToHistory === 'function') saveToHistory(historyExpr, '', '', calcMoney(finalAmount));
}


function getCustomThemes() { try { return JSON.parse(localStorage.getItem('hogar_calc_custom_themes') || '[]'); } catch(e) { return []; } }
function setCustomThemes(themes) { localStorage.setItem('hogar_calc_custom_themes', JSON.stringify(themes)); }
function saveCustomTheme() {
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
}

function renameCurrentCustomTheme() {
  if (!currentCustomTheme) return;
  const newName = prompt('Nombre para tu diseño:', currentCustomTheme.name || 'Mi Diseño');
  if (!newName || newName === currentCustomTheme.name) return;
  
  const themes = getCustomThemes();
  if (themes.some(t => t.name === newName)) {
     alert('Ya existe un diseño con ese nombre.');
     return;
  }
  
  currentCustomTheme.name = newName;
  if (currentCustomTheme.id) {
     const idx = themes.findIndex(t => t.id === currentCustomTheme.id);
     if (idx !== -1) {
        themes[idx].name = newName;
        setCustomThemes(themes);
        renderThemes();
     }
  }
  
  // Show the new name in the edit bar immediately
  document.getElementById('edit-mode-target').innerText = newName;
  
  if (currentCustomTheme.id) {
      alert('Diseño renombrado a: ' + newName);
  } else {
      alert('Nombre establecido. Recuerda Guardar para no perder los cambios.');
  }
}

function deleteCurrentCustomTheme() {
  if (!currentCustomTheme || !currentCustomTheme.id) {
    alert('Este diseño aún no está guardado, no se puede borrar.');
    return;
  }
  if(confirm('¿Estás seguro de que quieres borrar este diseño guardado?')) {
    const themes = getCustomThemes();
    const idx = themes.findIndex(t => t.id === currentCustomTheme.id);
    if (idx !== -1) {
      themes.splice(idx, 1);
      setCustomThemes(themes);
      renderThemes();
      toggleEditMode();
    }
  }
}
function deleteCustomTheme(index) {
  if(confirm('¿Estás seguro de que quieres borrar este diseño guardado?')) {
    const themes = getCustomThemes();
    themes.splice(index, 1);
    setCustomThemes(themes);
    renderThemes();
  }
}
function renderThemes() {
  const palette=document.getElementById('calculator-palette');
  if(!palette) return;
  let html = CALCULATOR_THEMES.map((theme,index)=>`<button class="calc-color" title="${theme.name}" style="background:linear-gradient(135deg,${theme.accent},${theme.display},${theme.opBottom})" onclick="setCalculatorTheme(CALCULATOR_THEMES[${index}]); toggleCalculatorPalette()"></button>`).join('');
  const custom = getCustomThemes();
  if (custom.length > 0) {
    html += '<div style="width:100%; height:1px; background:rgba(0,0,0,0.1); margin:4px 0;"></div>';
    html += custom.map((theme,index)=>`<div class="calc-color-custom" style="position:relative; display:inline-block;"><button class="calc-color" style="background:linear-gradient(135deg,${theme.accent||'#ccc'},${theme.display||'#eee'},${theme.opBottom||'#ddd'})" onclick="setCalculatorTheme(getCustomThemes()[${index}]); toggleCalculatorPalette()"></button><span class="calc-color-tooltip">${theme.name}</span></div>`).join('');
  }
  palette.innerHTML = html;
}

// Init
window.onload = () => {
  CALC_SOUND=lsGet('hogar_calc_sound')==='1';
  const palette=document.getElementById('calculator-palette');
  renderThemes();
  try{const saved=JSON.parse(lsGet('hogar_calc_theme')||'null');if(saved)setCalculatorTheme(saved);}catch(e){}
  document.querySelectorAll('#calculator-grid .calc-key,.calculator-display-actions .calc-mini-key[data-calc]').forEach(button=>button.onclick=()=>handleCalcKey(button.dataset.calc));
  loadHistory();
  updateCalc();
};

let isEditMode = false;
let currentCustomTheme = null;
let currentEditType = 'shell';

function toggleEditMode() {
  isEditMode = !isEditMode;
  const btn = document.getElementById('edit-mode-btn');
  const topBar = document.querySelector('.calc-top-bar');
  const editBar = document.getElementById('edit-top-bar');
  
  if (isEditMode) {
    document.body.classList.add('edit-mode');
    btn.innerHTML = '🛑 Salir Diseño';
    btn.style.background = '#4A90E2';
    topBar.style.display = 'none';
    editBar.style.display = 'flex';
    
    currentEditType = 'shell';
    document.getElementById('edit-mode-target').innerText = 'Fondo';
    document.getElementById('edit-color-picker').value = '#ffffff';

    if (!currentCustomTheme) {
      let active = JSON.parse(localStorage.getItem('hogar_calc_theme'));
      currentCustomTheme = { name: 'Mi Diseño' };
      if (active) Object.assign(currentCustomTheme, active);
      currentCustomTheme.name = 'Mi Diseño';
    }
    setTimeout(() => {
      alert('🎨 MODO DISEÑO INICIADO\n\n1. Toca cualquier botón o parte de la calculadora para seleccionarlo.\n2. Arriba verás lo que has seleccionado (ej. "Números").\n3. Toca el cuadradito blanco de arriba para elegir el color.');
    }, 150);
  } else {
    document.body.classList.remove('edit-mode');
    btn.innerHTML = '🖌️ Modo Diseño';
    btn.style.background = '#1ABC9C';
    topBar.style.display = 'flex';
    editBar.style.display = 'none';
  }
}

function handleEditModeSelect(type, val) {
  if (typeof event !== 'undefined' && event) {
    if (event.target.closest('.calc-colors-actions') || event.target.closest('#calc-colors-overlay') || event.target.closest('#edit-top-bar')) return;
    event.stopPropagation();
  }

  let editType = '';
  let name = '';
  if (type === 'display') { editType = 'display'; name = 'Pantalla'; }
  else if (type === 'shell') { editType = 'shell'; name = 'Fondo'; }
  else if (type === 'toolpanel') { editType = 'toolpanel'; name = 'Fondo Panel Descuento'; }
  else if (type === 'toolpanel_inputs') { editType = 'toolpanel_inputs'; name = 'Cajas de Texto'; }
  else if (type === 'toolpanel_calc_btn') { editType = 'toolpanel_calc_btn'; name = 'Botón Calcular'; }
  else if (type === 'toolbtn_discount') { editType = 'toolbtn_discount'; name = 'Botón Descuento'; }
  else if (type === 'toolbtn_increase') { editType = 'toolbtn_increase'; name = 'Botón Aumento'; }
  else if (type === 'toolbtn_vat') { editType = 'toolbtn_vat'; name = 'Botón IVA'; }
  else if (type === 'easteregg') { editType = 'easteregg'; name = 'Frase Motivadora'; }
  else if (type === 'key') {
     editType = 'key_' + val;
     name = 'Botón ' + val;
  }
  
  if (editType) {
    currentEditType = editType;
    document.getElementById('edit-mode-target').innerText = name;
    
    let hex = '#ffffff';
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
                 let baseAccent = currentCustomTheme.accent || defT.accent || hex;
                 // Compute a 55% mix of baseAccent and 45% white to match CSS color-mix exactly
                 hex = mixHexWithWhite(baseAccent, 0.45);
              } else if (btn.classList.contains('clear')) {
                 hex = currentCustomTheme.clearTop || defT.clearTop || hex;
              } else {
                 hex = currentCustomTheme.numTop || defT.numTop || hex;
              }
           }
         }
      }
    }
    
    if (/^#[0-9A-F]{6}$/i.test(hex)) {
      document.getElementById('edit-color-picker').value = hex;
    } else {
      document.getElementById('edit-color-picker').value = '#ffffff';
    }
  }
}

function hexToRgb(hex) {
  let c = hex.substring(1);
  if(c.length === 3) c = c.split('').map(x=>x+x).join('');
  return [parseInt(c.substr(0,2),16), parseInt(c.substr(2,2),16), parseInt(c.substr(4,2),16)];
}

function rgbToHex(r,g,b) {
  return "#" + ((1<<24)+(r<<16)+(g<<8)+b).toString(16).slice(1);
}

function adjustBrightness(hex, factor) {
  let [r,g,b] = hexToRgb(hex);
  r = Math.max(0, Math.min(255, r * factor));
  g = Math.max(0, Math.min(255, g * factor));
  b = Math.max(0, Math.min(255, b * factor));
  return rgbToHex(Math.round(r), Math.round(g), Math.round(b));
}

function applyCustomColor(type, baseHex) {
  if(!currentCustomTheme) currentCustomTheme = {name:'Mi Diseño'};
  
  if (type === 'display') {
    currentCustomTheme.display = baseHex;
    currentCustomTheme.displayText = adjustBrightness(baseHex, 0.2);
  } else if (type === 'shell') {
    currentCustomTheme.shellTop = baseHex;
    currentCustomTheme.shellBottom = adjustBrightness(baseHex, 0.9);
  } else if (type === 'toolpanel_bg') { currentCustomTheme.toolPanelBg = baseHex; } else if (type === 'toolpanel') {
    currentCustomTheme.toolPanel = baseHex;
  } else if (type === 'toolpanel_inputs') {
    currentCustomTheme.toolInputs = baseHex;
  } else if (type === 'toolpanel_calc_btn') {
    currentCustomTheme.toolCalcBtn = baseHex;
  } else if (type === 'toolbtn_discount') {
    currentCustomTheme.toolBtnDiscount = baseHex;
  } else if (type === 'toolbtn_increase') {
    currentCustomTheme.toolBtnIncrease = baseHex;
  } else if (type === 'toolbtn_vat') {
    currentCustomTheme.toolBtnVat = baseHex;
  } else if (type === 'easteregg') {
    currentCustomTheme.easterEgg = baseHex;
  } else if (type.startsWith('key_')) {
    let keyVal = type.substring(4);
    if (!currentCustomTheme.keys) currentCustomTheme.keys = {};
    currentCustomTheme.keys[keyVal] = {
      top: baseHex,
      bottom: adjustBrightness(baseHex, 0.85),
      shadow: adjustBrightness(baseHex, 0.65)
    };
  }
  
  setCalculatorTheme(currentCustomTheme);
  lsSet('hogar_calc_theme', JSON.stringify(currentCustomTheme));
}
