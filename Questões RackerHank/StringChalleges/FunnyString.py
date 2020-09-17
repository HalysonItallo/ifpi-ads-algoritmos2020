from auxString import reverse_text

def main():
  q = int(input())
  for _ in range(q):
    s = input()
    funnyString(s)

  
def funnyString(s):
  last_num_s = 0
  num_s = 0
  result_s = []
  
  #reverso
  r = reverse_text(s)
  
  last_num_r = 0
  num_r = 0
  result_r = []
  
  count_result = 0
  for i in range(len(s)):
    last_num_s = num_s
    num_s = ord(s[i])
    if i != 0:
      if num_s - last_num_s < 0:
        result_s.append((num_s - last_num_s)*-1)
      else:
        result_s.append(num_s - last_num_s)
      
    last_num_r = num_r
    num_r = ord(r[i])
    if i != 0:
      if  (num_r - last_num_r) < 0:
        result_r.append((num_r - last_num_r)*-1)
      else:
        result_r.append(num_r - last_num_r)
      
      
  for j in range(len(result_s)):
    if result_s[j] == result_r[j]:
      count_result += 1
   
   
  if count_result == len(result_s):
    print('Funny')
  else:
    print('Not Funny')
    
    
main()