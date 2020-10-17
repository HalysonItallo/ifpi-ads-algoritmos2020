def main():
  n = input('Digite seu número de 8 elementos na base binária: ')
  if len(n) != 8:
    print('Digite um número válido')
  else:
    conversion(n)


def conversion(n):
  count = 0
  while count < 8:
    if n[count] == '0' or n[count] == '1':
        hexadecimal = hex(int(n,2)) 
        integer = int(n,2)
    else:
      print('Digite um número válido')
      break
    count += 1
  print(f"A conversão para hex: {hexadecimal.replace('0x','')}")
  print(f'A conversão para int: {integer}')
   
   
main()