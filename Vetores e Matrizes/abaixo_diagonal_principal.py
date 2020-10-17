def main():
  O = input('S - soma | M - média: ')
  array = [[0] * 11]*11
  print(itens_below_diagonal(array,O))
  print(array)
  
  
def itens_below_diagonal(array,element): 
 
  count = 0
  for i in range(11):
    for j in range(11):
      archive = open('input.txt')
      for line in archive:
        if j > i:
          array[i][j] = int(line)
      # element = float(input('Digite o elemento: '))
  if element == 'S':
    return count
  elif element == 'M':
    return count / 66 
  archive.close()


main()