def main():
  number= int(input('Digite o número limite para os resultados das frações: '))
  calc_fraction(number)
  
  
def calc_fraction(number):
  result = 0
  count = 1
  while count <= number:
    if number < 1:
      print('Digite um valor válido.')
    else:
      if (count % 2 == 0):
        result -= (1/count)
      else:
        result += (1/count)
      count += 1
  print(result)


main()