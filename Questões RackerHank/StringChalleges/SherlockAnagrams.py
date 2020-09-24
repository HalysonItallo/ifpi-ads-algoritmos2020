#Build SherlockAnagrams

def main():
  q = int(input())
  for _ in range(q):
    s = input()
    sherlockAndAnagrams(s)

  
def sherlockAndAnagrams(s):
  # one_anagram(s)
  
  aux_s = s
  double_anagram = []
  for i in range(len(s)):
    if i+2 <= len(s):
      if aux_s[i] != aux_s[i+1]:
        double_anagram.append(aux_s[i:i+2])
    else: 
      print('dale')
    # aux_s = aux_s.replace(aux_s[i], '')
  print(double_anagram)


def one_anagram(s):
  one_anagram = []
  aux_s = s
  for i in range(len(aux_s)):
    for j in range(1,len(aux_s)):
      if aux_s[i] == aux_s[j]:
        one_anagram.append([aux_s[i], aux_s[j]])
        aux_s = aux_s.replace(aux_s[i], '')
  return one_anagram
    
    
main()
