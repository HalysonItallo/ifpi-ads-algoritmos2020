def main():
  numero = int(input('Digite um número que se aproxima de um quadrado perfeito: '))
  square_perfect(numero)
  
  
def square_perfect(numero):
  result = 0
  for i in range(1, numero):
    if result < numero:
      print(result)
      result = i * i
     
  
main()