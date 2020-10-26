import pickle
import json
import cell_db    
import selected_cell_component
  
def Add(name, mark, screen, value, cam_frontal):
  cell = {
  "nome": name,
  "marca": mark,
  "tela": screen,
  "valor": value,
  "cam_frontal": cam_frontal
  }
  cell_db.create(json.dumps(cell)) 


def Edit(name, mark, screen, value, cam_frontal, key):
  cell = {
  "nome": name,
  "marca": mark,
  "tela": screen,
  "valor": value,
  "cam_frontal": cam_frontal
  }
  cell_db.edit(key, json.dumps(cell)) 


def List():
  cell_db.read()
  
  
def Delete(key):
  cell_db.delete(key)


def Search(search_name):
  selected_cell_component.main(search_name)


def Show(search_name):
  return cell_db.show(search_name)
  
  
def ShowCell(key):
  cell_db.show_cell(key)


def Duplicated(key):
  cell_db.duplicate(key)

if __name__ == "__main__":
  Search('Sam')