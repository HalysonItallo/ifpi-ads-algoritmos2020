def main():
  number = int(input("Digite um número para calcular o seu fatorial: "))
  factorial(number)

def factorial(number):
  result = 1  
  for i in range(1, number+1, 1):
    result = result * i
  print('Seu fatorial: ', result) 
   


main()