
lista_numeros = []

menu =  """
sim
não
"""

numeros_usuario = input('digite os numeros que desaja acrescentar à lista separados por espaço: ')
fatiamento = numeros_usuario.split()
lista_numeros.append(fatiamento)

print(lista_numeros)