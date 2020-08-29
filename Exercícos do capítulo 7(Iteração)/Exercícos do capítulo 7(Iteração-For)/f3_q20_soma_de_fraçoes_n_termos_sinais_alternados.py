def main():
  number= int(input('Digite o número limite para os resultados das frações: '))
  calc_fraction(number)
  
  
def calc_fraction(number):
  result = 0
  for i in range(1, number+1, 1):
    if number < 1:
      print('Digite um valor válido.')
    else:
      if (i % 2 == 0):
        result -= (1/i)
      else:
        result += (1/i)
  print(result)


main()