def main():
  number= int(input('Digite o número limite da soma das frações: '))
  
  calc_fraction(number)
  
  
def calc_fraction(number):
  result = 0
  for i in range(0, number, 1):
    result += (i + 1) / (number - i)
  print(result)


main()