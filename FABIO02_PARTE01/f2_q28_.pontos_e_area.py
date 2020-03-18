def main():
    x1 = int(input("Qual o x do 1 ponto: "))
    y1 = int(input("Qual o Y do 1 ponto: "))
    
    x2 = int(input("Qual o x do 2 ponto: "))
    y2 = int(input("Qual o Y do 2 ponto: "))
    
    print(calc_area(x1, y1, x2, y2))
    
    
def calc_area(x1, y1, x2, y2):

    if (x1 != x2 and y1 != y2):
        base = x2 - x1
        altura = y2 - y1
        area = base * altura
        
        if area < 0:
            area * -1
        
        return area
    else:
        return "Pontos válidos para o calculo da área"
    

main()