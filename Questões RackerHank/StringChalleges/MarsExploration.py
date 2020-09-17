def main():
  s = input()
  marsExploration(s)
  

def marsExploration(s):
  aux_s = ''
  count_result = 0
  for i in range(len(s)):
    aux_s += s[i]
    if i % 3 == 2:
      if aux_s[0] != 'S':
        count_result += 1
      if aux_s[1] != 'O':
        count_result += 1
      if aux_s[2] != 'S':
        count_result += 1
      aux_s = ''
  print(count_result)
        
  
main()