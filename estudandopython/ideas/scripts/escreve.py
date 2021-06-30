def printlog(file_name, word, color='Reset'):
    """
    Write and save a text to file. 
    Possible colours to apear only in sys.stdout:
    Black, Red, Gree, Yellow, Blue, Magenta, Cyan, Light Gray, Dark Grey, Light Red, Light Green, Light Yellow, Light Blue, Light Magenta, Light Cyan, White, Bold, Reverses and by default a Reset colour.
    """
    with open(file_name + '.txt', 'a') as f:
        if color == 'Black':
            print('\033[1;30m' + word + '\033[0;0m')
        elif color == 'Red':
            print('\033[1;31m' + word + '\033[0;0m')
        elif color == 'Green':
            print('\033[1;32m' + word + '\033[0;0m')
        elif color == 'Yellow':
            print('\033[1;33m' + word + '\033[0;0m')
        elif color == 'Blue':
            print('\033[1;34m' + word + '\033[0;0m')
        elif color == 'Magenta':
            print('\033[1;35m' + word + '\033[0;0m')
        elif color == 'Cyan':
            print('\033[1;36m' + word + '\033[0;0m')
        elif color == 'Light Gray':
            print('\033[1;37m' + word + '\033[0;0m')
        elif color == 'Dark Grey':
            print('\033[1;90m' + word + '\033[0;0m')
        elif color == 'Light Red':
            print('\033[1;91m' + word + '\033[0;0m')
        elif color == 'Light Green':
            print('\033[1;92m' + word + '\033[0;0m')
        elif color == 'Light Yellow':
            print('\033[1;93m' + word + '\033[0;0m')
        elif color == 'Light Blue':
            print('\033[1;94m' + word + '\033[0;0m')
        elif color == 'Light Magenta':
            print('\033[1;95m' + word + '\033[0;0m')
        elif color == 'Light Cyan':
            print('\033[1;96m' + word + '\033[0;0m')
        elif color == 'White':
            print('\033[1;97m' + word + '\033[0;0m')
        elif color == 'Bold':
            print('\033[1;1m' + word + '\033[0;0m')
        elif color == 'Reverses':
            print('\033[1;7m' + word + '\033[0;0m')
        else:
            print('\033[0;0m' + word + '\033[0;0m')

        print(file=f.writelines(word))


teste = 5
printlog('saida_do_teste', f'testando para ver se funcionou {teste}', 'black')
printlog('saida_do_teste',
         '\033[1;30mverificando se tem saida que apaga a linha de cima\033[0;0m')
print('teste')
