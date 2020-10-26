import dbm
import json

def create(cell):
  db = dbm.open('cell.db', 'c')
  db[f'{len(db)}'] = cell 
  print('Celular criado com sucesso !!!')
  db.close()


def read():
  array = []
  count = 0
  db = dbm.open('cell.db', 'c')
  for line in db:
    value = json.loads(db.get(line))
    value['id'] = count 
    array.append(value)
    count += 1
  db.close()
  if not array:
    print('Valor de persquisa não encontrado')
  print(array) 


def delete(key):
  try: 
    db = dbm.open('cell.db', 'c')
    del db[key]
    print('O valor foi deletado com sucesso !!!')
    db.close()
  except KeyError:
    print('O valor de chave passado não existe')


def show(key):
  str_result = ''
  count = 0
  key.islower()
  db = dbm.open('cell.db', 'c')
  for line in db:
    result_db = json.loads(db.get(line))
    if (key in result_db['nome']) or (key in result_db['marca']):
      str_result += f'{result_db["nome"].capitalize()} | valor para pesquisa: {count}\n'
    count += 1
  db.close()
  return str_result
  

def show_cell(key):
  try:
     db = dbm.open('cell.db', 'c')
     result_db = json.loads(db.get(key))
     print(result_db)
     db.close()
  except TypeError:
    print('Valor de persquisa não encontrado')


def edit(key, cell):
  db = dbm.open('cell.db', 'c')
  db[key] = cell 
  print('Registro editado com sucesso !!!')
  db.close()


def duplicate(key):
  try:
    db = dbm.open('cell.db', 'c')
    cell_db = db.get(key)
    db[f'{len(db)}'] = cell_db 
    print('Registro duplicado com sucesso !!!')
    db.close()
  except TypeError:
    print('Valor de persquisa não encontrado')

if __name__ == "__main__":
  show('')