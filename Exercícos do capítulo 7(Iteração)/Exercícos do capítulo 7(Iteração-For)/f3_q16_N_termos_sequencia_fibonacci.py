def main():
  number = int(input('Digite o número que representará o tamanho da sequência: ')) 
  build_sequence(number)
  
  
def build_sequence(number):
  last_result = 1
  value = 0
  if number < 2:
   print("Por favor digite um número válido")
  else:
   for _ in range(0, number,1):
       print(value)
       result = value + last_result
       # update values
       value = last_result
       last_result = result
 
      
main()