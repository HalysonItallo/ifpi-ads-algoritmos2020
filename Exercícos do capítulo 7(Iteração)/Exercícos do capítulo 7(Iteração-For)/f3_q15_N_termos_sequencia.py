def main():
  number = int(input('Digite o núemero que representará o tamanho da sequência: ')) 
  build_sequence(number)
  
  
def build_sequence(number):
  last_result = 1
  result = 0
  for i in range(1, number+1, 1):
    if i == 1:
      result = 1
    else:
      result = last_result + i
      last_result = result
    print(result)


main()