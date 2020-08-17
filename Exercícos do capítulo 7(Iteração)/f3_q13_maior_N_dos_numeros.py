def main():
  number  = [int(x) for x in input("Digite uma lista de N números: ").split()]
  bigger_number(number)
  
  
def bigger_number(number):
  aux_number = number[0]
  count = 1
  while count < len(number):
    if aux_number < number[count]:
      aux_number = number[count]
    count += 1
  print(aux_number)
  
  
main()