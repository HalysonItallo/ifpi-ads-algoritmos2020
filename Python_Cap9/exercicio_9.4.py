def main():
  word = input("Digite uma palavra para ser verificada: ")
  letters = input("Digite um conjunto de letras que deverá está na palavra")
  
  print(uses_only(word, letters))


def uses_only(word, letters):
  for i in range(len(word)):
    if word[i] in letters:
      return True
    else:
      return False
  
  
main()