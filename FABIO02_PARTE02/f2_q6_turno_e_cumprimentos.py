def main():
    turno = input("Qual o turno em que você estuda? ")
    
    print(verificar_turno(turno))
    
    
def verificar_turno(turno):
    if turno == "M":
        return "Bom Dia"   
    elif turno == "V":
        return "Boa Tarde"
    elif turno == "N":
        return "Boa Noite"
    else:
        return "Valor Inválido" 
        
        
main()