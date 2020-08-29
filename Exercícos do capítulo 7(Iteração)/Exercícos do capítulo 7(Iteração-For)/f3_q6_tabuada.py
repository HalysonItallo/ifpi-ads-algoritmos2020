def main():
  start = 1
  end = 100
  equalize = 0
  
  for i in range(start, end, 1):
    result = start * (i - equalize)
    print(f'{start} x {(i - equalize)} = {result}')
   
    if i % 10 == 0:
      equalize += 10
      print(f'fim da tabuada do {start}')
      start += 1
      result = 0
    

main()