def main():
    do_twice(print_spam,10)
    do_twice(print_spam,10)


def do_twice(func, value):
    func() 
    func() 


def print_spam():
    print('spam')


main()