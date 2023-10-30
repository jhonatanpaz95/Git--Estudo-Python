
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




print(lista_nomes)
print(f'O numero total de nomes na lista é: {len(lista_nomes)}')

for nome in lista_nomes:
    print(nome)
 
    
