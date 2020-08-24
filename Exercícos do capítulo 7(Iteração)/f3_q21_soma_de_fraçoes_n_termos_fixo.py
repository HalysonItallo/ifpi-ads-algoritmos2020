def main():
  number= int(input('Digite o número limite da soma das frações: '))
  calc_fraction(number)
  
  
def calc_fraction(number):
  result = 1
  count = 1
  while count <= number:
    result +=  ((count*2) - 1) / count
    count += 1 
  print(result)


main()