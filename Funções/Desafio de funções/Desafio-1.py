



lista_numeros = [0]

while True:
    
    lista_numeros.append(int(input('digite um numero')))
    
    break

media_lista = sum(lista_numeros) / len(lista_numeros) 
print(f'{media_lista: .2f}')