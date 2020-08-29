def main():
  limit_number = int(input('Digite um número limite para a sequência númerica: '))
  buid_sequence(limit_number)
  

def buid_sequence(limit_number): 
  for i in range(1, limit_number+1, 1):
    if i % 2 == 0: 
      print(i) 


main()