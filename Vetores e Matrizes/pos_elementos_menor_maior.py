def main():
  array= []  
  n = int(input("Insira a quantidade de elementos do array: ")) 

  for _ in range(n): 
    element = int(input("Insira o elemento: "))
    array.append(element) 
  print("Menor valor do array:",min(array))
  print("Maior valor do array:",max(array))


main()