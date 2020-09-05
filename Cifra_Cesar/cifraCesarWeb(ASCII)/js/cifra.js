const text = document.getElementById('text-cifra');
const number = document.getElementById('number-cifra');
const button = document.getElementById('button');
const content = document.getElementById('show-result');

function buildText(text, indice, displacementNumber) {
  const posLetterDisplace = text.charCodeAt(indice) + displacementNumber;
  const posLetter = text.charCodeAt(indice);
  let resultAphabet = '';
  if (65 <=  posLetter && posLetter <= 90) { 
    if (posLetterDisplace < 65 && displacementNumber < 0) {
      resultAphabet = String.fromCharCode(90 + (posLetterDisplace - 64));
    } else if (90 < posLetterDisplace && displacementNumber > 0 ){
      resultAphabet = String.fromCharCode((posLetterDisplace - 90) + 64);
    } else { 
      resultAphabet = String.fromCharCode(posLetterDisplace);
    }
  }
  if (97 <=  posLetter && posLetter <= 122) { 
    if (posLetterDisplace < 97 && displacementNumber < 0) {
      resultAphabet = String.fromCharCode(122 + (posLetterDisplace - 96));
    } else if (122 < posLetterDisplace && displacementNumber > 0 ){
      resultAphabet = String.fromCharCode((posLetterDisplace - 122) + 96);
    } else { 
      resultAphabet = String.fromCharCode(posLetterDisplace);
    }
  }
  if (posLetter == 32) { 
    resultAphabet = ' '; 
  }
  
  return resultAphabet;
}

function rotateWord(e) {
  e.preventDefault();
  const displacementNumber = Number(number.value);
  content.innerHTML = '';
  
  let unencryptedText = '';
  
  for(let i = 0; i < text.value.length; i++) {
    unencryptedText += buildText(text.value, i, displacementNumber);
  } 
  
  const showText = document.createElement('h3');
  showText.textContent = unencryptedText;
  content.appendChild(showText);
}

button.addEventListener('click', rotateWord);

