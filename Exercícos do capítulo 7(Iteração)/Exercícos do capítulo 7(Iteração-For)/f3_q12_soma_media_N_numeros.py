def main():
  number  = [int(x) for x in input("Digite uma lista de N números: ").split()]
  print(f'A soma dos N números: {sum_numbers(number)} \nA média é: {average_numbers(number)}')
  
  
def sum_numbers(number):
  result = 0
  
  for i in number:
    result += i
  return result


def average_numbers(number): 
  return sum_numbers(number) / len(number)
  
  
main()


 