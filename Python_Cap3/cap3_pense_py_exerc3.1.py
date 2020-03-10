def main():
    right_justify("monty")


def right_justify(s):
    tamanho_palavra = 70-len(s)
    print(" "*tamanho_palavra+s)


main()