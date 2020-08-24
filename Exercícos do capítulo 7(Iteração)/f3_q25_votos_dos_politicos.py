def main():
  vote = [int(vote) for vote in input("Insira o voto da população colocando uma ',' para separar: ").split(",")]  
  
  compute_data(vote)


def compute_data(vote):
  candidate1 = 0
  candidate2 = 0
  candidate3 = 0
  null_vote = 0
  white_vote = 0
  count = 0
  
  while count < len(vote):
    if vote[count] == 1:
      candidate1 += 1
    elif vote[count] == 2:
      candidate2 += 1
    elif vote[count] == 3:
      candidate3 += 1
    elif vote[count] == 9:
      null_vote += 1
    elif vote[count] == 0:
      white_vote += 1
    else:
      print(f'Por favor o eleitor {count+1} ratifique o seu voto')
    count += 1
      
  print(f'Voto(s) do candidato 1: {candidate1}\nVoto(s) do candidato 2: {candidate2}\nVoto(s) do candidato 3: {candidate3}')
  print(f'Voto(s) nulo: {null_vote}\nVoto(s) branco: {white_vote}')
  
  if candidate1 > (candidate2 and candidate3): 
    print('O candidato 1 venceu')
  elif candidate2 > (candidate1 and candidate3):
    print('O candidato 2 venceu')
  elif candidate3 > (candidate1 and candidate2):
     print('O candidato 3 venceu')
  else:
    print('Segundo turno')
  
  
  
main()