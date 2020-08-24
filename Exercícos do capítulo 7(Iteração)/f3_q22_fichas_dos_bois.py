def main():
    identification = [int(identification) for identification in input("Insira os números de identificação de cada boi colocando uma ',' para separar: ").split(",")] 
    name =  [str(name) for name in input("Insira os nomes de cada boi colocando uma ',' para separar: ").split(",")] 
    weight =[int(weight) for weight in input("Insira os pesos de cada boi colocando uma ',' para separar: ").split(",")]
    
    aligment_weight(identification, name, weight)
    
    
def aligment_weight(identification, name, weight):
  position_high = 0
  position_low = 0
  aux_low_weight = weight[len(weight) - 1]
  aux_high_weight = weight[0]
  count = 0
  
  while count < len(weight):
    if aux_high_weight < weight[count]:
      position_high = count
      aux_high_weight = weight[count]
    if aux_low_weight > weight[count]:
      position_low = count
      aux_low_weight = weight[count] 
    count += 1
    
  print(f'O boi com maior peso: \nIdentification: {identification[position_high]} | Nome: {name[position_high]} | Peso: {aux_high_weight}')
  print(f'O boi com menor peso: \nIdentification: {identification[position_low]} | Nome: {name[position_low]} | Peso: {aux_low_weight}')
  

main()