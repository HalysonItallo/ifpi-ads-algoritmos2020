def main():
    angulo1 = int(input("Insira o primeiro valor: ")) 
    angulo2 = int(input("Insira o segundo  valor: "))
    angulo3 = int(input("Insira o terceiro valor: "))
    
    print(tipo_triangulo(angulo1, angulo2, angulo3))
    
    
def verificar_triangulo(angulo1, angulo2, angulo3):
    soma_angulos = angulo1 + angulo2 + angulo3
    if soma_angulos == 180 and (angulo1 or angulo2 or angulo3) != 0:
        return True
    else:
        return False
        
        
def tipo_triangulo(angulo1, angulo2, angulo3):
    if verificar_triangulo(angulo1, angulo2, angulo3):
        if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
            return "Acutângulo"
        elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
            return "Retângulo"
        elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
            return "Obtusângulo"
    else:
        return "Insira um valor válido"
            
            
main()