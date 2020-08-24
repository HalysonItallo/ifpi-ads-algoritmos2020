def main():
  number= int(input('Digite o número limite da soma das frações: '))
  
  calc_fraction(number)
  
  
def calc_fraction(number):
  result = 0
  count = 0
  while count < number:
    result += (count + 1) / (number - count)
    count += 1
  print(result)


main()