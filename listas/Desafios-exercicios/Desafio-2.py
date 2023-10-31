
lista_nomes = []

acrescentar_nomes = '''
[1] sim
[2] não
'''

while True:

    opcao = input(f'Deseja adicionar nomes para a lista? {acrescentar_nomes}digite: ')
    
    try:
        if opcao == 'sim':
            nome = input('Digite o nome e a tecla enter para adicionar o nome a lista.\nNomes: ')
            lista_nomes.append(nome)
        elif opcao == 'não':
            break
        elif opcao != ('sim' or 'não'):
            print('digite uma opção valida!')
    except ValueError:
        print('não é possivel adicionar numeros a lista')


string_mais_curta = min(lista_nomes, key=len)
string_maior = max(lista_nomes, key=len)
total_caracteres = sum(len(s) for s in lista_nomes)
Media_caracteres = round(total_caracteres / len(lista_nomes)) 

print(f'a média de caracteres arredontado para o numero inteiro mais proximo é: {Media_caracteres}')

print(f'os nomes da lista são:\n{lista_nomes}')

print(f'O numero total de nomes na lista é: {len(lista_nomes)}')

print(f'O nome mais curto da lista é: ({string_mais_curta})')

print(f'O maior nome da lista é: ({string_maior})')

