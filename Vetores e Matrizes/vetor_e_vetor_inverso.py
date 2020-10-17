def main():
  array: list = []  
  n: int = int(input("Insira a quantidade de elementos do array: ")) 

  for _ in range(n): 
      element: str = input("Insira o elemento: ")
      
      array.append(element)   
  
  vector_inverse(array)
  
def vector_inverse(array: list) -> list:
  aux_array = []
  for i in range(len(array)-1, -1, -1):
    aux_array.append(array[i])
  print(aux_array)
  

main()