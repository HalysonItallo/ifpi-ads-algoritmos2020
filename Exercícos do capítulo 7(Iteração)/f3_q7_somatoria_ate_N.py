def main():
  number = int(input('Digite o número limite da sua somatória: '))
  summation(number)
  
def summation(number):
  end_number = number
  start_number = 1
  counter = 1
  while counter < end_number:
    counter += 1                       
    start_number += counter
  print(start_number)
    
  
main()
