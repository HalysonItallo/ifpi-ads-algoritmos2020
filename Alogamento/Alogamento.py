def main():
  n = int(input('Quantos digitos você pretende digitar? '))
  
  array = vector_default(n)
  for i in range(n):
    number = int(input('Insira o número desejado: '))
    array[i] = number
  
  print(show_qtd(array))
  
  if qtd_negative(array) <= qtd_positive(array):
    array = double_array(array)
  else:
    array = half_array(array)
  
  print(show_qtd(array))
  
  print(f'\nA média dos valores: {arithmetic_average(array)}')
  
  
def show_qtd(array: list) -> str:
  return f'\nqtd Par: {qtd_pair(array)} | qtd Ímpar: {qtd_odd(array)}' \
  + f'| qtd Negativos: {qtd_negative(array)} | qtd Positivos: {qtd_positive(array)}'
  
  
def vector_default(n: int) -> list:
  array = []
  count = 0
  while count < n: 
    array.append(-1)
    count += 1
  return array


def qtd_pair(array: list) -> int:
  count_result = 0
  for i in range(len(array)):
    if array[i] % 2 == 0:
      count_result += 1
  return count_result
  
  
def qtd_odd(array: list) -> int:
  count_result = 0
  for i in range(len(array)):
    if array[i] % 2 != 0:
      count_result += 1
  return count_result
  
  
def qtd_negative(array: list) -> int:
  count_result = 0
  for i in range(len(array)):
    if array[i] < 0:
      count_result += 1
  return count_result
  
  
def qtd_positive(array: list) -> int:
  count_result = 0
  for i in range(len(array)):
    if array[i] >= 0:
      count_result += 1
  return count_result
  
  
def double_array(array: list) -> list:
  for i in range(len(array)):
    array[i] = array[i] * 2
  return array


def half_array(array: list) -> list:
  for i in range(len(array)):
    array[i] = array[i] / 2
  return array


def arithmetic_average(array: list):
  value = 0
  for i in range(len(array)):
    value += array[i]
  return value/len(array)
  
     
main()