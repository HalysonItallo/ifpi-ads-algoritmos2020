def main():
  count = 0
  forbidden_letters = [forbidden_letters for forbidden_letters in input('Digite as letras proibidas: ').split(',')]
  
  file = open('words.txt')
  
  for line in file:
    word = line.strip()
    if avoid(word, forbidden_letters):
      count += 1  
  print(count) 
  file.close()
  
 
def avoid(word, forbidden_letters):
  for i in range(len(word)):
    if word[i] in forbidden_letters:
        return False
    return True
    
    
main()