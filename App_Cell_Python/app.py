import os
import sys
import controller

def main():
  menu = '*** Brincando com Arquivos de dados ***'
  menu += '\n 1 - Inserir valores: '
  menu += '\n 2 - Mostrar todos os valores: '
  menu += '\n 3 - Buscar Celular por parte do nome ou parte do nome da marca: '
  menu += '\n 0 - Sair'
  menu += '\n\n Opção >>> '

  while True: 
    opcao = int(input(menu))
    if opcao == 1:
      name = input('Nome: ')
      mark = input('Marca: ')
      screen = input('Tela("): ')
      value = float(input('Valor R$: '))
      cam_frontal = input('Camera frontal(sim/não): ')
      
      controller.Add(name.lower(), mark.lower(), screen.lower(), value, cam_frontal.lower())
    
    elif opcao == 2:
      controller.List()
    elif opcao == 3:
      key = input('Insira a parte do nome ou parte do nome da marca que você deseja buscar: ')
      controller.Search(key)
    elif opcao == 0:  
      break
      
    input('<enter> to continue... \n ')
      
          
main()