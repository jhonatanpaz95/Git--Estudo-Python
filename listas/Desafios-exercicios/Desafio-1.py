
# O programa recebe 5 numeros do usuário, acrescenta em uma lista e mostra na tela a posição e o numero.

lista_de_numeros =[]

while len(lista_de_numeros) < 5:
    try:
        numeros_usuario = int(input('digite 5 numeros: '))
        lista_de_numeros.append(numeros_usuario)
        print(f'A lista possui esses numeros até o momento {lista_de_numeros}')
    except ValueError:
        print('Erro! Não é possivel adicionar letras ou valores booleanos')

for indice, numero in enumerate(lista_de_numeros, start=1):

    print(f'Na posição {indice} tem o numero {numero}')