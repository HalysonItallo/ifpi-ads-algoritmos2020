def main():
    perg_01 = input("Telefonou para a vítima ? S/N ")
    perg_02 = input("Esteve no local do crime ? S/N ")
    perg_03 = input("Mora perto da vítima ? S/N ")
    perg_04 = input("Devia para a vítima ? S/N ")
    perg_05 = input("Já trabalhou com a vítima ? S/N ")
    
    print(analisar_suspeita(perg_01, perg_02, perg_03, perg_04, perg_05))
    
def verificar_respostas(perg_01, perg_02, perg_03, perg_04, perg_05):
    sentenca01 = perg_01 == "S" or perg_01 == "N" or perg_01 == "s" or perg_01 == "n" 
    sentenca02 = perg_02 == "S" or perg_02 == "N" or perg_02 == "s" or perg_02 == "n"
    sentenca03 = perg_03 == "S" or perg_03 == "N" or perg_03 == "s" or perg_03 == "n"
    sentenca04 = perg_04 == "S" or perg_04 == "N" or perg_04 == "s" or perg_04 == "n"
    sentenca05 = perg_05 == "S" or perg_05 == "N" or perg_05 == "s" or perg_05 == "n"
    if sentenca01 and sentenca02 and sentenca03 and sentenca04 and sentenca05:
        return True
    else:  
        return "Por favor responda um valor de resposta válido"
    
    
    
def analisar_suspeita(perg_01, perg_02, perg_03, perg_04, perg_05):
    text = ''
    if perg_02 == "S" or perg_02 == "s":
        text = "Suspeita\n"
    elif (perg_03 == "S" and perg_04 == "S") or  (perg_03 == "s" and perg_04 == "s"):
        text += "Cúmplice\n"
    elif perg_05 == "S" or perg_05 == "s":
        text += "Assasino\n"
    else:
        text = "Inocente"
    
    return text


main()