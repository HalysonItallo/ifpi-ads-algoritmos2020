def main():
    limit_dowm = int(input('Digite o limite inferior: '))
    limit_up = int(input('Digite o limite superior: '))
    
    calc_prime(limit_dowm, limit_up)


def calc_prime(limit_dowm, limit_up):
    if 0 < limit_dowm: 
        for i in range(limit_dowm+1, limit_up, 1):     
            multiple = 0
            for j in range(2, i, 1):
                if (i % j == 0):
                    multiple += 1  
            if(multiple==0):
                print(i)  
    else:
        print('Digite um valor válido.')        
        
        
main()

