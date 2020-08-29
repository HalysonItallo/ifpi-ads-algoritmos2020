def main():
  number  = [int(x) for x in input("Digite uma lista de N números: ").split()]
  bigger_number(number)
  
  
def bigger_number(number):
  aux_number = number[0]
  
  for i in number:
    if aux_number < i:
      aux_number = i
  print(aux_number)
  
  
main()