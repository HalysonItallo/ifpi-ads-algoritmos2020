def main():
    salario = float(input("Qual o seu salário: "))
    
    print(verificar_salario(salario))
    
    
def aumentar_salario(salario, porcentagem):  
    calc_porcentagem = (salario * porcentagem) / 100
    return calc_porcentagem


def escrever_tela(salario,porcentagem):
    aumento = aumentar_salario(salario,porcentagem)
    novo_salario = salario + aumento
        
    text1 = f"\nSalário antes do ajuste {salario} R$\nAumento de {porcentagem}%" 
    tetx2 = "\nO aumento no salário {} R$\nNovo salário depois do ajuste {} R$\n".format(aumento,novo_salario)
        
    return text1 + tetx2
    
    
def verificar_salario(salario):
    if 0 <= salario <= 280:
        return escrever_tela(salario,20) 
    elif 280 < salario <= 700:
        return escrever_tela(salario,15)
    elif 700 < salario <= 1500:
        return escrever_tela(salario,10)
    elif 1500 < salario:
        return escrever_tela(salario,5)
main()