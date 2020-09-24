def main():
  menu = 'Options for Words \n' \
      + '*****************\n' \
      + 'Digite 1 - Para obter a opção de exibir as palavras com mais de 20 letras\n' \
      + 'Digite 2 - Para obter a opção de exibir as palavras sem a letra "e"\n' \
      + 'Digite 3 - Para obter a opção de exibir a qunatidade de palavras sem as letras que' \
      + 'você deseja(usando a virgula para separá-las)\n' \
      + '\nDigite a opção desejada: ' \
      + '\n'

  menu_option = int(input(menu))
  continue_routine = 1
  count = 0
  while continue_routine != 2:
    if continue_routine == 1:
      if count != 0:
        menu_option = int(input(menu)) 
      if menu_option == 1:
        more_twenty_letters()
      elif menu_option == 2:
        show_has_no_e()
      elif menu_option == 3:
        show_avoid()
      else:
          print('Opção Inválida!')
    else:
      print('Opção Inválida!')
    continue_routine = int(input('\nVocê deseja continuar digite [1] para sim ou [2] para não: ')) 
    count += 1
  print('Encerrado...')


def more_twenty_letters():
  file = open('words.txt')
  for line in file:
    word = line.strip()
    if len(word) > 20:
      print(word)


def show_has_no_e():
  count_total = 0
  count_no_e = 0
  calc_per = 0.0
  file = open('words.txt')
  for line in file:
    word = line.strip()
    count_total += 1
    if has_no_e(word):
      count_no_e += 1
      print(word)
  calc_per = (count_no_e/count_total)*100
  print("{:.2f}".format(calc_per))
  
  
def has_no_e(word):
  for i in range(len(word)):
    if word[i] == 'e':
      return False
  return True


def show_avoid():
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