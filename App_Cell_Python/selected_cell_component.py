import controller

def main(search_name):
  menu = '\n 1 - Mostrar detalhes: '
  menu += '\n 2 - Remover: '
  menu += '\n 3 - Editar: '
  menu += '\n 4 - Duplicar registro: '
  menu += '\n 0 - Voltar'
  menu += '\n\n Opção >>> '

  while True:  
    if controller.Show(search_name) == '':
      print('valor de pesquisa não encontrado \n')
      break
    print(controller.Show(search_name))
  
    key = input('\nInsira o valor de pesquisa: ') 
    
    opcao = int(input(menu))
    if opcao == 1:
      controller.ShowCell(key)
    elif opcao == 2:
      controller.Delete(key)
    elif opcao == 3:
      name = input('Nome: ')
      mark = input('Marca: ')
      screen = input('Tela("): ')
      value = float(input('Valor R$: '))
      cam_frontal = input('Camera frontal(sim/não): ')
      
      controller.Edit(name.lower(), mark.lower(), screen.lower(), value, cam_frontal.lower(), key)
    elif opcao == 4:
      controller.Duplicated(key)
    elif opcao == 0:  
      break
    input('<enter> to continue... \n ')
