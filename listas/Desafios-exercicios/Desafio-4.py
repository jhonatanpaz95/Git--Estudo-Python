
lista_de_palavras = []


entrada_usuario = input('digite as palavras ou frases que gostaria de acrescentar a lista serparados por (,): ')


lista_de_palavras = [str(nome) for nome in entrada_usuario.split(',')]
print(lista_de_palavras)



# contar quantas palavras ou frases tem na lista. (fazer isso pelo indice)
quantidade_frases = len(lista_de_palavras)
print(f'Existem {quantidade_frases} frases na lista.')


# Saber a MAIOR palavra:
maior_palavra = ""

for palavra in lista_de_palavras:

    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra

print(f'A maior palavra ou frase da lista é: {maior_palavra}')

# Saber a MENOR palavra:
menor_palavra = None

for palavra in lista_de_palavras:
    if menor_palavra is None or len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print(f'A menor palavra ou frase da lista é: {menor_palavra}')

