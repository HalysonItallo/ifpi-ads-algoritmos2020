def main():
  limit_dowm = int(input('Digite o limite inferior: '))
  limit_up = int(input('Digite o limite superior: '))
  number_multiple = int(input('Digite um número que definirá o múltiplo: '))
  
  calc_multiple(limit_up, limit_dowm, number_multiple)
  
  
def calc_multiple(limit_up, limit_dowm, number_multiple):
  for i in range(limit_dowm, limit_up, 1):
    if i % number_multiple == 0 and i != limit_up:
      print(i)
  
  
main()