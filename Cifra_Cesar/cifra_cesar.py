def main():
  texto_criptografado  = input('Digite o texto que deseja criptografar: ')
  num_casas = int(input('Qual o deslocamento da criptografia? '))
  
  rotate_word(num_casas,texto_criptografado)

def rotate_word(num_casas, texto_criptografado):
    alfabeto_minusculo = ["a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    alfabeto_maiusculo = ["A","B","C","D","E","F","G","H","I","J",
    "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    texto_descriptografado = "" 
    for i in range(len(texto_criptografado)):
        for j in range (len(alfabeto_minusculo)):
            if texto_criptografado[i] == alfabeto_minusculo[j]:
                texto_descriptografado += alfabeto_minusculo [j+num_casas]
            elif texto_criptografado[i] == alfabeto_maiusculo[j]:
                texto_descriptografado += alfabeto_maiusculo [j+num_casas]
            elif texto_criptografado[i] == " " and j == len(alfabeto_minusculo) - 1:
                texto_descriptografado += " "
            elif texto_criptografado[i] == " " and j == len(alfabeto_maiusculo) - 1:
                texto_descriptografado += " "
    print(texto_descriptografado)
            
main()