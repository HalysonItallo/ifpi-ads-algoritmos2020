def main():
    num = int(input("Qual o seu número: "))
    
    print(quantidade_decompositores(num))
    

def quantidade_decompositores(num):
    if num < 1000:
        text = ''
        
        milhar = num // 1000
        num -= milhar * 1000
        
        centena = num // 100
        num -= centena * 100
        
        dezena = num // 10
        num -= dezena * 10
        
        if milhar != 0:
            text = f"{milhar} milhar(es), "
        if centena != 0:
            text += f"{centena} centena(s), "
        if dezena != 0:
            text += f"{dezena} dezena(s) "
      
        if dezena == 0 and num != 0:
            text += f"{num} unidade(s)"
        elif num != 0:
            text += f"e {num} unidade(s)"
        
        return text
        
        
main()