def main():
  code = [int(code) for code in input("Insira o de código de cada funcionário colocando uma ',' para separar: ").split(",")] 
  work_hours = [int(work_hours) for work_hours in input("Insira as horas trabalhadas de cada funcionário colocando uma ',' para separar: ").split(",")] 
  number_dependents =[int(number_dependents) for number_dependents in input("Insira os número de dependentes de cada funcionário colocando uma ',' para separar: ").split(",")]
  
  payment_employee(code, work_hours, number_dependents)
  
  
def payment_employee(code, work_hours, number_dependents): 
  for i in range(0, len(code), 1):
    total = (12 * work_hours[i]) + (40 * number_dependents[i])
    discount_INSS = (total * 8.5) / 100
    discount_IR = (total * 5) / 100
    
    print(f'Desconto do INSS: {discount_INSS}, Desconto IR: {discount_IR}, Valor líquido {total-(discount_INSS + discount_IR)}')


main()