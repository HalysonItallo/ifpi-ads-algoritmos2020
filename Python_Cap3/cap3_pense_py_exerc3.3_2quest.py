#chama minha tabela
def main():
    grid(4,4)
    
    
#aumenta o lado da tabela junto com a função side
def upper(value = 0):
    row = "+ - - - - +"
    add = row + " - - - - +" * value
    return add
    
    
#aumenta o lado da tabela junto com a função upper    
def side(value = 0):
    column = "|         |"
    add = column + "         |" * value
    return add
    
    
# aumenta a parte de baixo da tabela
def low(size_low,size_row):
    add = side(size_row) + "\n"
    add += upper(size_row) + "\n"
    return add 
   
   
# printa a tabela   
def grid(size_row = 1, size_column = 1):
    print(upper(size_row))
    print(low(size_column,size_row) * size_column)


main()