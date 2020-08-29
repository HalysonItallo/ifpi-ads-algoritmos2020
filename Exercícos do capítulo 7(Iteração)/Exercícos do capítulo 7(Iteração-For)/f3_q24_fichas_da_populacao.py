def main():
  salary = [int(salary) for salary in input("Insira o salário da população colocando uma ',' para separar: ").split(",")] 
  quant_son =  [int(quant_son) for quant_son in input("Insira a quantidade de filhos da população colocando uma ',' para separar: ").split(",")] 

  search_population(salary, quant_son)
  
  
def search_population(salary, quant_son): 
  if len(salary) != len(quant_son):
    print('Verifique os dados inseridos.')
  else:
    percentage = 0
    total_salary = 0
    total_quant_son = 0
    
    for i in range(0, len(salary), 1):
      total_salary += salary[i]
      total_quant_son += quant_son[i]
      if salary[i] < 1000:
        percentage += 1
    average_salary = (total_salary / len(salary))
    average_quant_son = (total_quant_son / len(quant_son))
    calc_percentage = round((percentage / len(salary)) * 100)
    
    print(f'a) Média de salário da população: {average_salary} ')
    print(f'b) Média de números de filhos: {average_quant_son}')
    print(f'c) Percentual de pessoas com salário de até R$ 1.000,00: {calc_percentage}%')
    
    
main()