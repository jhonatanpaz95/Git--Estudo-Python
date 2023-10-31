
# Programa recebe os nomes do usuário e armazena em uma lista.
# O obejtivo do programa é saber quantos nomes tem na lista, o maior e o menor nome e saber a média de caracteres.

lista_nomes = []

acrescentar_nomes = '''
[1] sim
[2] não
'''
# Laço de repetição que recebe os nomes da lista.
while True:

    opcao = input(f'Deseja adicionar nomes para a lista? {acrescentar_nomes}digite: ')
    
    
    if opcao == 'sim':
        nome = input('Digite o nome e a tecla enter para adicionar o nome a lista.\nNomes: ')
        if nome.isalpha():
            lista_nomes.append(nome)
        else:
            print('Digite um nome válido (apenas letras).')
    elif opcao == 'não':
        break
    else:
        print('digite uma opção valida!')


# funcionalidades (quantos nomes tem na lista, o maior e o menor nome e média de caracteres).

try:
    string_mais_curta = min(lista_nomes, key=len)
    string_maior = max(lista_nomes, key=len)
    total_caracteres = sum(len(s) for s in lista_nomes)
    Media_caracteres = round(total_caracteres / len(lista_nomes))

    print(f'a média de caracteres arredontado para o numero inteiro mais proximo é: {Media_caracteres}')

    print(f'os nomes da lista são:\n{lista_nomes}')

    print(f'O numero total de nomes na lista é: {len(lista_nomes)}')

    print(f'O nome mais curto da lista é: ({string_mais_curta})')

    print(f'O maior nome da lista é: ({string_maior})')

except ValueError:
    print(f'A lista está fazia! adicione nomes para ter um resultado mais eficaz.')


