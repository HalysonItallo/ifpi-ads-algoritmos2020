def main():
  limit_number = int(input('Digite um número limite para a sequência númerica: '))
  buid_sequence(limit_number)
  

def buid_sequence(limit_number): 
  counter = 0 
  while counter < limit_number:
    counter += 1
    print(counter) 
 

main()