from auxString import contains 
# Build Gattaca(2 / 11 casos)

def main():
  n = int(input())
  if ((4 <= n and n <=5000000) and (n % 4 == 0)):
    gene = input()
    stableGene(gene)
  

def stableGene(gene):
  qtd_A = 0
  qtd_C = 0
  qtd_T = 0
  qtd_G = 0
  diff_go = []
  
  for i in range(len(gene)):
    if gene[i] in 'A':
      if qtd_A < (len(gene) / 4):
        qtd_A += 1
      else:
        diff_go.append('A')
        if qtd_T < (len(gene) / 4):
          qtd_T += 2
        elif qtd_C < (len(gene) / 4):
          qtd_C += 2
        elif qtd_G < (len(gene) / 4):
          qtd_G += 2
            
    elif gene[i] in 'C':
      if qtd_C < (len(gene) / 4):
        qtd_C += 1
      else:
        diff_go.append('C')
        if qtd_G < (len(gene) / 4):
          qtd_G += 2
        elif qtd_A < (len(gene) / 4):
          qtd_A += 2
        elif qtd_T < (len(gene) / 4):
          qtd_T += 2
        
        
    elif gene[i] in 'T':
      if qtd_T < (len(gene) / 4):
        qtd_T += 1
      else:
        diff_go.append('T')
        if qtd_C < (len(gene) / 4):
          qtd_C += 2
        elif qtd_G < (len(gene) / 4):
          qtd_G += 2
        elif qtd_A < (len(gene) / 4):
          qtd_A += 2
        
    elif gene[i] in 'G':
      if qtd_G < (len(gene) / 4):
        qtd_G += 1
      else:
        diff_go.append('G')
        if qtd_A < (len(gene) / 4):
          qtd_A += 2
        elif qtd_T < (len(gene) / 4):
          qtd_T += 2
        elif qtd_C < (len(gene) / 4):
          qtd_C += 2
        
    print(f'A: {qtd_A} | T: {qtd_T} | C: {qtd_C} | G: {qtd_G}')
    print(diff_go)
    
  
  
main()