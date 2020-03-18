def main():
    senha = int(input("Digite a senha: "))
    
    print(verificar_senha(senha))
    
    
def verificar_senha(senha):
    if senha == 1234:
        return "Acesso permitido"
    else:
        return "Acesso negado"


main()