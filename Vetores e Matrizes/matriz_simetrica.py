def main():  
  n = int(input("Insira o tamanho da matriz quadratica: ")) 
  transposed_array = []
  array = []
  for _ in range(n):
    array.append([0] * n)
    transposed_array.append([0] * n)
    
  build_matrix(array, transposed_array)
  
  if array == transposed_array:
    print('A matriz é simétrica')
  else:
    print('A matriz não é simétrica')
  
  
def build_matrix(array, transposed_array):
  for i in range(len(array)):
    for j in range(len(array[i])):
      element = int(input(f'Digite o elemento que corresponde a linha {i+1} e a coluna {j+1}: '))
      array[i][j] = element
      transposed_array[j][i] = element
 
      
main()