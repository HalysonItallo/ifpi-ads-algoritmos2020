def main():

  menu = '*** Brincando com Listas ***'
  menu += '\n 1 - Inserir Valores'
  menu += '\n 2 - Mostrar Valor posição'
  menu += '\n 3 - Mostrar todos os valores'
  menu += '\n 4 - Remover do Final'
  menu += '\n 5 - Remover do Início'
  menu += '\n 6 - Remover de Posição Específica'
  menu += '\n 7 - Inserir valores em Posição Específica'
  menu += '\n 8 - Contagem Qtd Pares'
  menu += '\n 9 - Contagem Qtd Ímpares'
  menu += '\n 10 - Contagem Qtd Primos'
  menu += '\n 11 - Contagenm Qtd Positivos' 
  menu += '\n 12 - Contagem Qtd Zerados'
  menu += '\n 13 - Média dos Valores'
  menu += '\n 14 - Ocorrências de um dado valor'
  menu += '\n 15 - Dobrar todos os valores --'
  menu += '\n 16 - Dobrar valores múltiplos de N'
  menu += '\n 17 - Apagar todos os valores'
  menu += '\n 0 - Sair '
  menu += '\n\n Opção >>> '

  lista = []

  while True: 
    opcao = int(input(menu))
    if opcao == 1:
      inserir_valores(lista)
    elif opcao == 2:
      mostra_valor(lista)
    elif opcao == 3:
      mostra_todos_valores(lista)
    elif opcao == 4:
      remover_final(lista)
    elif opcao == 5:
      remover_inicio(lista)
    elif opcao == 6:
      remover_posicao(lista)
    elif opcao == 7:
      inserir_valores_posição(lista)
    elif opcao == 8:
      qtd_par(lista)
    elif opcao == 9:
      qtd_impar(lista)
    elif opcao == 10:
      qtd_primo(lista)
    elif opcao == 11:
      qtd_positivo(lista)
    elif opcao == 12:
      qtd_zerados(lista)
    elif opcao == 13:
      media(lista)
    elif opcao == 14:
      qtd_numero(lista)
    elif opcao == 15:
      dobrar_valores(lista)
    elif opcao == 16:
      dobrar_valores_multiplos_n(lista)
    elif opcao == 17:
      apagar_todos_valores(lista)
    elif opcao == 0:  
      break
    else:
      print('Opção Inválida')


def inserir_valores(lista):
  qtd = int(input('Quantos valores desejar inserir? '))

  for _ in range(qtd):
    valor = int(input('Valor: '))
    lista.append(valor)

  print('Valores inseridos com sucesso! ')
  input('<enter> to continue...')
  


def mostra_valor(lista):
  posicao = int(input('Qual posição? '))
  print('Valor buscado:')
  print(lista[posicao])

  input('<enter> to continue...')


def mostra_todos_valores(lista):

  if not lista:
    print('Sua lista está vazia')
  else:
    aux_lista = ''
    for i in range(len(lista)):
      if i != len(lista)-1:
        aux_lista += str(lista[i]) + ', '
      else:  
        aux_lista += str(lista[i])
        
    print('Valores:')
    print(aux_lista)
  
  input('<enter> to continue...')
    
    
def remover_final(lista):
  if not lista:
    print('Sua lista está vazia')
  else:
    lista.remove(lista[len(lista)-1])
    
  print('Elemento removido do final com sucesso!')
    
  input('<enter> to continue...')
    
def remover_inicio(lista):
  if not lista:
    print('Sua lista está vazia')
  else:
    lista.remove(lista[0])
    
  print('Elemento removido do Início com sucesso!')
  
  input('<enter> to continue...')
  

def remover_posicao(lista):
  if not lista:
    print('Sua lista está vazia')
  else:
    posicao = int(input('Qual a posição que você quer remover? '))
    lista.remove(lista[posicao])
    
  print('Elemento removido da posição com sucesso!')
  
  input('<enter> to continue...')


def inserir_valores_posição(lista):
  qtd = int(input('Quantos valores desejar inserir? '))

  for _ in range(qtd):
    pos = int(input('Posição: '))
    valor = int(input('Valor: '))
    lista.insert(pos, valor)

  print('Valores inseridos nas posições com sucesso! ')
  
  input('<enter> to continue...')


def qtd_par(lista) :
  contador_par = 0
  for i in range(len(lista)):
    if lista[i] % 2 == 0:
      contador_par += 1
      
  print('A quantidade de par:')
  
  print(contador_par)
  
  input('<enter> to continue...')


def qtd_impar(lista) :
  contador_impar = 0
  for i in range(len(lista)):
    if lista[i] % 2 != 0:
      contador_impar += 1
      
  print('A quantidade de Ímpar:')
  
  print(contador_impar)
  
  input('<enter> to continue...')


def eh_primo(primo):
  qtd_divisores = 0
  numero = 1
  while numero <= primo:
    if primo % numero == 0:
        qtd_divisores += 1
    numero += 1
  
  if qtd_divisores == 2:
    return True
  else:
    return False
      
      
def qtd_primo(lista):
  contador_primo = 0
  for i in range(len(lista)):
    if eh_primo(lista[i]):
      contador_primo += 1
  
  print('A quantidade de primos:')
    
  print(contador_primo)
  
  input('<enter> to continue...')
  

def qtd_positivo(lista):
  contador_positivo = 0
  for i in range(len(lista)):
    if lista[i] >= 0:
      contador_positivo += 1
      
  print('A quantidade de positivos:')
  
  print(contador_positivo)
  
  input('<enter> to continue...')
  
 
def qtd_zerados(lista):
  contador_zerado = 0
  for i in range(len(lista)):
    if lista[i] == 0:
      contador_zerado += 1
      
  print('A quantidade de zeros:')
  
  print(contador_zerado)
  
  input('<enter> to continue...')
  

def media(lista):
  valor = 0
  for i in range(len(lista)):
    valor += lista[i]
 
  print('A media:')
  
  print(valor/len(lista))
  
  input('<enter> to continue...')
  
  
def qtd_numero(lista):
  contador_numero = 0
  numero = int(input('Digite o número que você quer contar ocorrências: '))
  for i in range(len(lista)):
    if lista[i] == numero:
      contador_numero += 1
      
  print(f'A quantidade de {numero}:')
  
  print(contador_numero)
  
  input('<enter> to continue...')


def dobrar_valores(lista):
  for i in range(len(lista)):
    lista[i] = lista[i] * 2
  
  print(f'O array com os valores dobrados:')
  
  print(lista)
  
  input('<enter> to continue...')


def dobrar_valores_multiplos_n(lista):
  multiplo = int(input('Digite o valor múltiplo de N: '))
  for i in range(len(lista)):
    if lista[i] % multiplo == 0:
      lista[i] = lista[i] * 2
  
  print(f'O array com os valores multiplos de N dobrados:')
  
  print(lista)
  
  input('<enter> to continue...')


def apagar_todos_valores(lista):
  lista.clear()
  
  print('Todos os elementos foram apagados')
    
  input('<enter> to continue...')

main()