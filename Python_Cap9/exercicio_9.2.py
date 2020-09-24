def main():
  count_total = 0
  count_no_e = 0
  calc_per = 0.0
  file = open('words.txt')
  for line in file:
    word = line.strip()
    count_total += 1
    if has_no_e(word):
      count_no_e += 1
      print(word)
  calc_per = (count_no_e/count_total)*100
  print("{:.2f}".format(calc_per))


def has_no_e(word):
  for i in range(len(word)):
    if word[i] == 'e':
      return False
  return True

main()