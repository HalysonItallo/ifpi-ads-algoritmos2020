def main():
  number= int(input('Digite o número limite para os resultados das frações: '))
  
  calc_fraction(number)
  
  
def calc_fraction(number):
  result = 0
  count1 = 1
  count2 = number
  while count1 <= number:
    if number < 1:
      print('Digite um valor válido.')
    else:
      if count2 % 2 == 0:
        result += (count1 / count2)
      else:
        result -= (count1 / count2)
      count1 += 1
      count2 -= 1
  print(result)
     

main()