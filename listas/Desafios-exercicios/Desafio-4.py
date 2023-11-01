
lista_de_palavras = []

entrada_usuario = input('digite as palavras ou frases que gostaria de acrescentar a lista serparados por (,): ')

lista_de_palavras = [str(nome) for nome in entrada_usuario.split(',')]
print(lista_de_palavras)

#print(entrada_usuario)
#lista_de_palavras.append(entrada_usuario)
#print(lista_de_palavras)