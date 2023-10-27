


def calcular_media(list) -> float:

    """ 
    Esta função calcula a média de uma lista de números.
    Retorna a média ou 0 se a lista estiver vazia 
    """

    lista_numeros = []

    menu = '''
    [1] sim
    [2] não 
    '''

    while True:

    
        opcao = input(f'Deseja acrescentar numeros a lista {menu}:')

        try:
            if opcao == 'sim':
                lista_numeros.append(int(input('digite os numeros da lista: ')))
            elif opcao == 'não':
              break
        except Exception as e:
            print(f'erro! você não digitou uma opção valida {e}. Digite novamente: ')

    print(f'a lista tem os seguintes numeros{lista_numeros}')

    try:
        resultado = sum(lista_numeros) / len(lista_numeros)
        print(f'a média da lista é: {resultado: .2f}')
        return resultado
    except ZeroDivisionError:
        print('A média é 0')


#calcular_media()


lista_nova = [2, 5, 8, 10]

calcular_media(lista_nova)