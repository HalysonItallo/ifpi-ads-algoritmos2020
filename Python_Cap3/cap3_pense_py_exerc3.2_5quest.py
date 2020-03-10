def main():
    do_four(print_spam,5)


def do_four(func,value):
    do_twice(func,value)
    do_twice(func,value)


def do_twice(func, value):
    func() 
    func() 


def print_spam():
    print('spam')


main()