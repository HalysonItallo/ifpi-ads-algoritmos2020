def main():
  numero = int(input('Digite um número que se aproxima de um quadrado perfeito: '))
  square_perfect(numero)
  
  
def square_perfect(numero):
  result = 0
  count = 1
  while True:
    if result <= numero:
      result = count * count
      count += 1
    else:
      print((count-2) * (count-2))
      break
     
  
main()