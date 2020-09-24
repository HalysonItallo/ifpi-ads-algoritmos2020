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
    
def is_upper(text: str) -> bool:
  alphabet = ["A","B","C","D","E","F","G","H","I","J",
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
    
    
def contains(text: str, comparison_text: str) -> bool:
  aux_text = ''
  count = 0 
  displace = 0
  while True:
    aux_text += text[displace+count]
    if len(aux_text) == len(comparison_text):
      if (aux_text == comparison_text):
        return True
      elif (displace+count) == len(text)-1:
        return False
      else:
        aux_text = ''
        displace += 1 
        count = -1
    elif (displace+count) == len(text)-1:
      return False
    count += 1
    
    
def slice_text(text: str, pos_in: int, pos_out: int) -> str:
  result_text = ''
  if pos_in < 0 or len(text) < pos_out:
    return ''
  else:
    for i in range(pos_in, pos_out, 1):
      result_text += text[i]
    return result_text
    
  
  
  