def main():
  A0 = int(input('Digite o A0 dá progressão aritmética: '))
  Limit = int(input('Digite o limite da progressão aritmética: '))
  R = int(input('Digite o R dá progressão aritmética: '))
  
  calc_geometric_progression(A0, Limit, R)
  
  
def calc_geometric_progression(A0, Limit, R):
    if A0 <= 0 or Limit <= A0:
      print('Por Favor digite um valor correto.')
    else:
      for i in range(A0, int(Limit / R)):
        i = i * R
        print(i)
    
  
main()