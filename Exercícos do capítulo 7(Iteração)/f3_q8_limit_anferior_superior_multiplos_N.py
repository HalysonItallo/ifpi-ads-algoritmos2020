def main():
  limit_dowm = int(input('Digite o limite inferior: '))
  limit_up = int(input('Digite o limite superior: '))
  number_multiple = int(input('Digite um número que definirá o múltiplo: '))
  
  calc_multiple(limit_up, limit_dowm, number_multiple)
  
  
def calc_multiple(limit_up, limit_dowm, number_multiple):
  number = limit_dowm
  while number < limit_up:
    number += 1
    if number % number_multiple == 0 and number != limit_up:
      print(number)
  
  
main()