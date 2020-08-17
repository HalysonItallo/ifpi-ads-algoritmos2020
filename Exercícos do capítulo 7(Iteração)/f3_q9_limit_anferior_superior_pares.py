def main():
  limit_dowm = int(input('Digite o limite inferior: '))
  limit_up = int(input('Digite o limite superior: '))
 
  
  calc_pair(limit_up, limit_dowm)
  
  
def calc_pair(limit_up, limit_dowm):
  number = limit_dowm
  while number < limit_up:
    number += 1
    if number % 2 == 0 and number != limit_up:
      print(number)
  
  
main()