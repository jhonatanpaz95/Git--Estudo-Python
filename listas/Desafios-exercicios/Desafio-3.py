
lista_numeros = []

menu =  """
sim
não
"""

while True:
    numeros_usuario = input('Digite os números que deseja acrescentar à lista separados por espaço: ')
    
    if numeros_usuario.replace(' ', '').isdigit():  # Verifica se a entrada contém apenas dígitos
        break  # Se a entrada é válida, sai do loop
    else:
        print("Por favor, insira apenas números válidos. Tente novamente.")

fatiamento = [int(numero) for numero in numeros_usuario.split()] # converte a entrada do usuário para numeros inteiros
lista_numeros = fatiamento
print(lista_numeros)

#Calcular a soma de todos os números na lista.

for numero in lista_numeros:
    numero += numero
    print(numero)