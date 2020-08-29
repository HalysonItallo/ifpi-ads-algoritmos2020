def main():
  limit_dowm = int(input('Digite o limite inferior: '))
  limit_up = int(input('Digite o limite superior: '))
 
  
  calc_pair(limit_up, limit_dowm)
  
  
def calc_pair(limit_up, limit_dowm):
  for i in range(limit_dowm, limit_up, 1):
    if i % 2 == 0 and i != limit_up:
      print(i)
  
  
main()