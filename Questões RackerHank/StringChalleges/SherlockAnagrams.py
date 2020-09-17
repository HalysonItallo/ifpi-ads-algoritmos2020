#Build SherlockAnagrams

def main():
  q = int(input())
  for _ in range(q):
    s = input()
    sherlockAndAnagrams(s)

  
def sherlockAndAnagrams(s):
  count = 1
  pair_anagrams = []
  while count < len(s):
    for i in range(0, len(s), count):
      for j in range(0, len(s), count):
        pair_anagrams.append([i,j])
    count += 1
  
  print(pair_anagrams)
  
    
main()
