# funções anonimas 
#Desafio 1: Dobrando Números
#Crie uma função lambda que recebe uma lista de números e retorna uma nova lista onde cada número foi dobrado.

lista_numeros = [5, 3, 2, 5, 8, 10]
dobra_lista = list(map(lambda x: x*2, lista_numeros))
print(dobra_lista)


# Desafio 2: Filtrando Números Pares
#Utilize a função filter com uma função lambda para filtrar apenas os números pares de uma lista de inteiros.

numero_pares = list(filter(lambda x: x % 2 == 0, lista_numeros))
print(numero_pares)

#Desafio 3: Calculando a Média
#Crie uma função lambda que calcule a média de uma lista de números.

