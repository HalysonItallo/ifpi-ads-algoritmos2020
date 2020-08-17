def main():
    limit_dowm = int(input('Digite o limite inferior: '))
    limit_up = int(input('Digite o limite superior: '))
    
    calc_prime(limit_dowm, limit_up)


def calc_prime(limit_dowm, limit_up):
    if 0 < limit_dowm: 
        count_between_limit = limit_dowm 
        while count_between_limit < limit_up:
            count_between_limit += 1
            multiple = 0
            counter = 2
            while counter < count_between_limit:
                if (count_between_limit % counter == 0):
                    multiple += 1  
                counter += 1
            if(multiple==0):
                print(count_between_limit)  
    else:
        print('Digite um valor válido.')        
        
        
main()

