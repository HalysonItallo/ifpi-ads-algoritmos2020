def main():
    do_twice(print,10)
    do_twice(print,10)


def do_twice(func, value):
    func(value) 
    func(value) 


main()