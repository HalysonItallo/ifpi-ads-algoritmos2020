def main():
  number= int(input('Digite o número limite da soma das frações: '))
  
  calc_fraction(number)
    
    
def calc_fraction(number):
  result = 0
  for i in range(1, number+1, 1):
    result += i ** -1  
  print(result)


main()