def main():
  n = int(input("Insira o tamanho da matriz quadratica: ")) 
  array = []
  for _ in range(n):
    array.append([0] * n)
  print(array)
  diagonal(array)


def diagonal(array):
  main_diagonal = 0 
  secondary_diagonal = 0
  no_diagonal = 0
  for i in range(len(array)):
    for j in range(len(array[i])):
      element = int(input(f'Digite o elemento que corresponde a linha {i+1} e a coluna {j+1}: '))
      array[i][j] = element
      if j == i:
        main_diagonal += element
      if (j+i+2) == (len(array) + 1):
        secondary_diagonal += element
      if (j!=i) and not ((j+i+2) == (len(array) + 1)):
        no_diagonal += element
  print(f'\nSomatória da diagonal principal: {main_diagonal}')
  print(f'Somatória da diagonal secundária: {secondary_diagonal}')
  print(f'Somatória dos números que não estão nas diagonais: {no_diagonal}')
        
           
main()