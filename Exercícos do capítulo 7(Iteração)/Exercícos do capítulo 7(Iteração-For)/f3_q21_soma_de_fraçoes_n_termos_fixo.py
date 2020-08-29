def main():
  number= int(input('Digite o número limite da soma das frações: '))
  calc_fraction(number)
  
  
def calc_fraction(number):
  result = 1
  for i in range(1, number+1, 1):
    result +=  ((i*2) - 1) / i
  print(result)


main()