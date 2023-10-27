


def media_lista() -> float:

    lista_numeros = []

    menu = '''
    [1] sim
    [2] não 
    '''

    while True:

    
        opcao = input(f' {menu}Deseja acrescentar numeros a lista:')

        if opcao == 'sim':
            lista_numeros.append(int(input('digite os numeros da lista: ')))
        elif opcao == 'não':
            break
        else:
            print('digite uma opção valida: ')

    print(f'a lista tem os seguintes numeros{lista_numeros}')

    try:
        media_lista = sum(lista_numeros) / len(lista_numeros)
        print(f'a média da lista é: {media_lista: .2f}')
        return media_lista
    except ZeroDivisionError:
        print('A média é 0')


media_lista()
