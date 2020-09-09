def is_aphabet(text: str) -> bool: 
  alphabet = ["a","b","c","d","e","f","g","h","i","j",
  "k","l","m","n","o","p","q","r","s","t","u","v","w",
  "x","y","z","A","B","C","D","E","F","G","H","I","J",
  "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  count = 0
  aux_text = ''
  while count < len(text):
    for i in range(len(alphabet)):
      if text[count] == alphabet[i]:
        aux_text += alphabet[i]
    count += 1
  
  if len(aux_text) == len(text): 
    return True
  else:
    return False
    
def reverse_text(text: str) -> str:
  aux_text = ''
  count = len(text)-1
  while count >= 0:
    aux_text += text[count]
    count -= 1
  return aux_text
    
    
  
  
  