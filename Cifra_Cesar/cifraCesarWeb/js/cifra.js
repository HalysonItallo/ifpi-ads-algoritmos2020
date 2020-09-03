const text = document.getElementById('text-cifra');
const number = document.getElementById('number-cifra');
const button = document.getElementById('button');
const content = document.getElementById('show-result');

function buildArray(index, alphabet, displacementNumber) {
  let resultAphabet = '';
  if (alphabet[index+displacementNumber] == undefined && displacementNumber >= 0) { 
    resultAphabet += alphabet[(displacementNumber - (alphabet.length - index))];
  } else if (alphabet[index+displacementNumber] == undefined && displacementNumber < 0) {
    resultAphabet += alphabet[alphabet.length + (displacementNumber + index)]; 
  }
  else {
    resultAphabet += alphabet[index+displacementNumber];
  }
  return resultAphabet;
}

function rotateWord(e) {
  e.preventDefault();
  
  const displacementNumber = Number(number.value);
  content.innerHTML = '';
  
  const lowercaseAlphabet = ["a","b","c","d","e","f","g","h","i","j",
  "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
  const uppercaseAlphabet = ["A","B","C","D","E","F","G","H","I","J",
  "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];

  let unencryptedText = '';
  
  for(let i = 0; i < text.value.length; i++) {
    for(let j = 0; j < lowercaseAlphabet.length; j++) {
      if(text.value[i] == lowercaseAlphabet[j]) {
        unencryptedText += buildArray(j, lowercaseAlphabet, displacementNumber);
      } else if(text.value[i] == ' ' && j == lowercaseAlphabet.length - 1) {
        unencryptedText += ' ';
      }  else if(text.value[i] == uppercaseAlphabet[j]) {
        unencryptedText += buildArray(j, uppercaseAlphabet, displacementNumber);
      }
      
    }
  } 
  let showText = document.createElement('h3')
  showText.textContent = unencryptedText
  content.appendChild(showText)
}

button.addEventListener('click', rotateWord)

