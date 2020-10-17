def main():  
  n: int = int(input("Insira o tamanho da matriz quadratica: ")) 
  array: list = []
  for _ in range(n):
    array.append([0] * n)
  print(array)
  insert_itens(array)
  print(array)
  
def insert_itens(array: list) -> list:
  for i in range(len(array)):
    for j in range(len(array[i])):
      element = int(input(f'Digite o elemento que corresponde a linha {i+1} e a coluna {j+1}: '))
      array[j][i] = element
  

main()