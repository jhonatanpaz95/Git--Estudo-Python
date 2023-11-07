# LER ARQUIVOS
media_idades = []

with open(file= r'C:\Users\Samsung\Desktop\Git- Estudo Python\Ler arquivos\CHATGPT.txt', mode='r', encoding='utf-8') as arquivo:
    linha = arquivo.readline()
    linha = arquivo.readline()
    while linha:
        linha_separada = linha.split(sep= ',')
        idade = linha_separada[1]
        idade = int(idade)
        media_idades.append(idade)
        linha = arquivo.readline()
     

print(media_idades)
media_idades = sum(media_idades) / len(media_idades)
print(media_idades)


