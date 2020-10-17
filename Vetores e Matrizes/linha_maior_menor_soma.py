def main():  
  n = int(input("Insira o tamanho da matriz quadratica: ")) 
  array = []
  insert_itens(array, n)
  print('Menor somátorio de uma linha',min(array))
  print('Maior somátorio de uma linha',max(array))
  
  
def insert_itens(array, n):
  count_line = 0
  for i in range(n):
    for j in range(n):
      element = int(input(f'Digite o elemento que corresponde a linha {i+1} e a coluna {j+1}: '))
      count_line += element
      if j+1 == n:
        array.append(count_line)
        count_line = 0
      

main()
      
