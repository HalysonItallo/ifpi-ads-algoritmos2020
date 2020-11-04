def show_menu(): 
  menu = '*** Eleições 2012 ***'
  menu += '\n OBS: Se não seguir a ordem de amostragem pode ser que os valores estejam equivocados'
  menu += '\n 1 - Mostrar coligações: '
  menu += '\n 2 - Mostrar todos os candidatos: '
  menu += '\n 3 - Mostrar total de votos: '
  menu += '\n 4 - Mostrar QE(Quociente Eleitoral): '
  menu += '\n 5 - Mostrar total de votos por coligação: '
  menu += '\n 6 - Mostrar quantidade de vagas por coligação e resto de vagas faltantes: '
  menu += '\n 7 - Vagas restantes adicionadas às coligações: '
  menu += '\n 8 - Vereadores eleitos de acordo com a eleição proporcional'
  menu += '\n 9 - Vereadores eleitos de acordo com a eleição não proporcional'
  menu += '\n 0 - Sair'
  menu += '\n\n Opção >>> '
  
  return menu

def show_format_informations(params):
  for info in params:
    print(info)  
    

def union(array_union):
  file = open('partidos_coligacoes_the_2012.txt', 'r')
  for line in file:
    array_union.append({ 'coligacao': line.strip(), 'total_votos': 0, 'qtd_vagas': 0, 'votos_sobra_total': 0 })
  file.close()


def candidate(array_candidate):
  file = open('candidatos_e_votos_vereador_THE_2012.txt', 'r')
  for line in file:
    archive = line.strip().split(';')
    array_candidate.append({'nome': archive[0], 
      'numero': archive[1], 'partido': archive[2], 
      'coligacao': archive[3], 'total_votos': archive[4] }) 
  
  file.close()
 
 
def sort_candidate(array_candidate):
  return sorted(array_candidate, key=lambda candidate_array: int(candidate_array['total_votos']), reverse=True)


def total_votes(array_candidate):
  result_votes = 0
  for item in array_candidate:
    result_votes += int(item['total_votos'])
  
  return result_votes


def total_votes_union(array_union, array_candidate):
  if not (array_union[len(array_union)-1]['total_votos'] == 47988):
    for union in array_union:
      for candidate in array_candidate:
          if union['coligacao'] == candidate['coligacao']:
            union['total_votos'] += int(candidate['total_votos'])
  return array_union
  

def total_vacancies(array_union, array_candidate):
  qe = round(total_votes(array_candidate) / 29)
  qtd_rest = 29
  for union in array_union:
    if int(union['total_votos']) >= qe:
      qtd_vacancies = round(int(union['total_votos']) / qe) 
      if union['qtd_vagas'] == 0 and union['votos_sobra_total'] == 0:
        union['qtd_vagas'] = qtd_vacancies
        union['votos_sobra_total'] = int(union['total_votos']) % qe
        qtd_rest -= qtd_vacancies
  return qtd_rest
  
  
def rest_vacancies(array_union, array_candidate, qtd_rest):  
  aux_array = [] 
  while qtd_rest != 0:
    for union in array_union:
      aux_array.append(round(int(union['total_votos']) / (union['qtd_vagas'] + 1)))
    array_union[aux_array.index(max(aux_array))]['qtd_vagas'] += 1 
    aux_array.clear()
    qtd_rest -= 1
  return qtd_rest
  

def candidates_elected_by_proportional_election(array_union, array_candidate):
  aux_array = []
  for union in array_union:
    aux_array.append({union['coligacao']: [],})
  
  for i in range(len(array_union)):
    for j in range(len(array_candidate)):
      if array_union[i]['coligacao'] == array_candidate[j]['coligacao']:
        aux_array[i][array_union[i]['coligacao']].append(array_candidate[j]) 
  result_array = []
  
  for i in range(len(array_union)):
    for _ in range(array_union[i]['qtd_vagas']):
      result_array.append(
      {
        'nome':  max(aux_array[i][array_union[i]['coligacao']], key=lambda array : int(array['total_votos']))['nome'],
        'nome_partido': max(aux_array[i][array_union[i]['coligacao']], key=lambda array : int(array['total_votos']))['partido'],
        'coligacao': max(aux_array[i][array_union[i]['coligacao']], key=lambda array : int(array['total_votos']))['coligacao'],
        'total_votos': max(aux_array[i][array_union[i]['coligacao']], key=lambda array : int(array['total_votos']))['total_votos'],
      })
      aux_array[i][array_union[i]['coligacao']].pop(aux_array[i][array_union[i]['coligacao']]
        .index(max(aux_array[i][array_union[i]['coligacao']], key=lambda array : int(array['total_votos']))))
  return result_array
      

def candidates_elected_by_non_proportional_election(array_candidate):
  aux_array = array_candidate.copy()
  result_array = []
  for _ in range(29):
    result_array.append(
    {
      'nome': max(aux_array, key=lambda array : int(array['total_votos']))['nome'],
      'nome_partido': max(aux_array, key=lambda array : int(array['total_votos']))['partido'],
      'coligacao':  max(aux_array, key=lambda array : int(array['total_votos']))['coligacao'],
      'total_votos': max(aux_array, key=lambda array : int(array['total_votos']))['total_votos']
    }) 
    aux_array.pop(aux_array.index(max(aux_array, key=lambda array : int(array['total_votos']))))
  
  return result_array