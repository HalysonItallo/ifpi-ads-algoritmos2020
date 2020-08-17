def main():
  number = int(input("Digite um número para calcular o seu fatorial: "))
  factorial(number)

def factorial(number):
  count = 1  
  result = 1  
  while count <= number:
      print(result)
      result = result * count 
      count += 1
  print('Seu fatorial: ', result) 


main()