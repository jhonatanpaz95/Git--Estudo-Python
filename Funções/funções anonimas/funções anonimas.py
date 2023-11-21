# funções anonimas

#Desafio 1: Dobrando Números
#Crie uma função lambda que recebe uma lista de números e retorna uma nova lista onde cada número foi dobrado.

lista_numeros = [5, 3, 2, 5, 8] 

nova_lista = list(map(lambda x: x*2, lista_numeros))
print(nova_lista)
