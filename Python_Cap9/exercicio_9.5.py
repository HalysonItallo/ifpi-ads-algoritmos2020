def main():
  word = input("Digite uma palavra para ser verificada: ")
  letters = input("Digite um conjunto de letras que deverá está na palavra")
  
  uses_all(word, letters)
  
def uses_all(word, mandatory_letters):
  for i in range(len(mandatory_letters)):
    if mandatory_letters[i] not in word:
      return False
  return True


main()