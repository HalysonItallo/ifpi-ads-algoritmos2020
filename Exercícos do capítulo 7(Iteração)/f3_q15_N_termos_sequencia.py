def main():
  number = int(input('Digite o núemero que representará o tamanho da sequência: ')) 
  build_sequence(number)
  
  
def build_sequence(number):
  last_result = 1
  result = 0
  count = 1
  while count <= number: 
    if count == 1:
      result = 1
      count += 1
    else:
      result = last_result + count
      last_result = result
      count += 1
    print(result)


main()