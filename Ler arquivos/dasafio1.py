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
    arquivo.close()

print(media_idades)
media_idades = sum(media_idades) / len(media_idades)
print(media_idades)


maior_receita = []

with open(file= r'C:\Users\Samsung\Desktop\Git- Estudo Python\Ler arquivos\CHATGPT.txt', mode='r', encoding='utf-8') as arquivo:
    arquivo.readline()
    linha = arquivo.readline()
    while linha:
        linha_separada = linha.split(sep=',')
        receita = linha_separada[3]
        receita = int(receita)
        maior_receita.append(receita)
        linha = arquivo.readline()

print(maior_receita)

maior =  None

for receita in maior_receita:
    maior = receita
    if receita > maior:
        print(receita)