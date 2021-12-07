def leiaDinheiro(msg):
    ok = False

    while not ok:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isalpha() or num =='':
            print(f'\033[0;31mERRO!{num} é um preço inválido.\033[m')
        else:
            ok = True
            return float(num)

