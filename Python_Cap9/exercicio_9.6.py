def main():
  word = input('Digite a palavra para saber se está em ordem alfabética')
  is_abecedarian(word)


def is_abecedarian(word):
  aux_word = word[0]
  for i in range(1,len(word)):
    if aux_word > word[i]:
      return False
    aux_word = word[i]
  return True


main()