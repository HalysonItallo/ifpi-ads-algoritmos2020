import os

def main():
  sed('Maca','Laranja','read.txt','write.txt')


def sed(string_default, replacement_string, name_read_file, name_write_file):
  aux_string = ''
  first_file = open(name_read_file, 'r')
  for line in first_file:
    if (os.path.exists(name_write_file)):
      second_file = open(name_write_file, 'w')
    else:
      second_file = open(name_write_file, 'x') 
    if line.strip() != string_default: 
      aux_string += line 
    else:
      aux_string += replacement_string + '\n'
  
  second_file.writelines(aux_string)
  first_file.close()
  second_file.close()
  
  
main()