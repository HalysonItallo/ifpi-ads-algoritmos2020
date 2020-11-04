import os
import features

def main():  
  #Inicialização
  array_union = []
  array_candidate = []
  qtd_rest = 0
  features.union(array_union)
  features.candidate(array_candidate)
  
  menu = features.show_menu()

  while True: 
    opcao = int(input(menu))
    if opcao == 1:
      features.show_format_informations(array_union)
    
    elif opcao == 2:
      features.show_format_informations(features.sort_candidate(array_candidate))
    
    elif opcao == 3:
      print(features.total_votes(array_candidate))
    
    elif opcao == 4:
      print(features.total_votes(array_candidate) // 29)
    
    elif opcao == 5:
      features.show_format_informations(features.total_votes_union(array_union, array_candidate))
    
    elif opcao == 6:
      # features.total_vacancies(array_union, array_candidate)
      qtd_rest = features.total_vacancies(array_union, array_candidate)
      print('Quantidade de vagas que ainda restam:', qtd_rest)
      features.show_format_informations(array_union)
    
    elif opcao == 7:  
      qtd_rest = features.rest_vacancies(array_union, array_candidate, qtd_rest)
      features.show_format_informations(array_union)
    
    elif opcao == 8:
      # features.candidates_elected_by_proportional_election(array_union, array_candidate)
      result = features.sort_candidate(features.candidates_elected_by_proportional_election(array_union, array_candidate)) 
      features.show_format_informations(result) 
    
    elif opcao == 9:
      result = features.sort_candidate(features.candidates_elected_by_non_proportional_election(array_candidate))
      features.show_format_informations(result) 
    
    elif opcao == 0:  
      break
      
    input('\n<enter> to continue... \n ')
    os.system('cls')
      

main()