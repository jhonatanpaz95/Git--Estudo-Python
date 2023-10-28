
lista_nomes = []

acrescentar_nomes = '''
[1] sim
[2] não
'''

while True:

    opcao = input(f'Deseja adicionar nomes para a lista? {acrescentar_nomes}: ')
    
    if opcao == 'sim':
        entrada = str(input('Digite os nomes e use espaço para separar os nomes da lista.\nNomes: '))
        nomes = entrada.split()
        lista_nomes. append(nomes)
        lista_nomes = [str(nome) for nome in nomes]

    elif opcao == 'não':
        break

    
print(lista_nomes)