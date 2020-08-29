def main():
  A0 = int(input('Digite o A0 dá progressão aritmética: '))
  Limit = int(input('Digite o limite da progressão aritmética: '))
  R = int(input('Digite o R dá progressão aritmética: '))
  
  calc_arithmetic_progression(A0, Limit, R)
  
  
def calc_arithmetic_progression(A0, Limit, R):
  if (Limit < A0) or (R <= 1):
    print('Por Favor digite um valor correto.')
  else:
    for i in range(A0, Limit, R):
      print(i)
    
  
main()