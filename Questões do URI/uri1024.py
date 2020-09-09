from auxString import *

def main():
  N = int(input())
  
  for _ in range(N):  
    M = input()  
    result_text = ''
    for j in M:
      posLetterDisplace = ord(j) + 3
      if is_aphabet(j): 
        result_text += chr(posLetterDisplace)
      else: 
        result_text += j    
    
    result_text = reverse_text(result_text)
    
    final_text = ''
    
    for k in range(len(result_text)):
      posLetterDisplace = ord(result_text[k]) - 1
      if len(result_text) // 2 <= k:
        final_text += chr(posLetterDisplace)
      else:
        final_text += result_text[k]
      
      
    print (final_text)
    
    
main()