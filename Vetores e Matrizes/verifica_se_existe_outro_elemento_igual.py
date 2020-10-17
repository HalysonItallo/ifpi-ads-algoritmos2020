def main():
  array= []  
  n = int(input("Insira a quantidade de elementos do array: ")) 

  for _ in range(n): 
      element = input("Insira o elemento: ")
      
      array.append(element)   

  if array_unique(array):
    print('Existe pelo menos um elemento igual')
  else:
    print('Não existe elemento(s) iguai(s)')
    
    
def array_unique(array: list) -> int:
  for i in range(len(array)):
    if array.count(array[i]) > 1:
      return True
  return False
  
  
main()