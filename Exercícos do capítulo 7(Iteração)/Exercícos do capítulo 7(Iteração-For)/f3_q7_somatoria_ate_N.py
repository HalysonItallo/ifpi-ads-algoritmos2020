def main():
  number = int(input('Digite o número limite da sua somatória: '))
  summation(number)
  
def summation(number):
  result = 1
  
  for i in range(2, number, 1):                       
    result += i
  print(result)
    
  
main()
