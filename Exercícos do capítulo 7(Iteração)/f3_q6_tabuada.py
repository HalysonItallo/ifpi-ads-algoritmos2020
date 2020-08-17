def main():
  start = 1
  end = 10
  counter = 0
  
  while start <= end:
    result = start * counter
    print(f'{start} x {counter} = {result}')
    counter += 1
    
    if counter == 10:
      counter = 0
      print(f'fim da tabuada do {start}')
      start += 1
      result = 0
      

main()