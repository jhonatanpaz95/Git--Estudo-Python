
lista_numeros = []

while True:
    numeros_usuario = input('Digite os números que deseja acrescentar à lista separados por espaço: ')
    
    if numeros_usuario.replace(' ', '').isdigit():  # Verifica se a entrada contém apenas dígitos
        break  # Se a entrada é válida, sai do loop
    else:
        print("Por favor, insira apenas números válidos. Tente novamente.")

fatiamento = [int(numero) for numero in numeros_usuario.split()] # converte a entrada do usuário para numeros inteiros
lista_numeros = fatiamento
print(lista_numeros)

# Calcula a soma de todos os números na lista.
soma_da_lista = sum(lista_numeros)
print(f'a soma dos numeros da lista é: {soma_da_lista}')

# verifica o maior numero
maior_numero = max(lista_numeros)
print(f'o maior numero da lista é: {maior_numero}')

# verifica o menor numero
menor_numero = min(lista_numeros)
print(f'o menor numero da lista é: {menor_numero}')

# soma do maior e menor numero:
soma_maior_menor = menor_numero + maior_numero
print(f'A soma do maior e do menor numero é: {soma_maior_menor}')