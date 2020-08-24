def main():
  number= int(input('Digite o número limite da soma das frações: '))
  
  calc_fraction(number)
    
    
def calc_fraction(number):
  result = 0
  count = 0
  while count < number:
    count += 1
    result += count ** -1
    
  print(result)

main()