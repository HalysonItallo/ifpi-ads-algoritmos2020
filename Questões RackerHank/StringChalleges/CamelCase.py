def main():
  s = input()
  camelCase(s)
  
  
def camelCase(s):
  count_camel_case = 0
  aphabet_upper = ["A","B","C","D","E","F","G","H","I","J",
  "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
  for i in range(len(s)):
    for j in range(len(aphabet_upper)):
      if s[i] == aphabet_upper[j]:
        count_camel_case +=1
  
  print(count_camel_case+1)
      


main()