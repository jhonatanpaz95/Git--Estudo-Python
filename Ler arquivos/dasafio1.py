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
    arquivo.close()

print(maior_receita)

maior =  None

for receita in maior_receita:
    maior = receita
    if receita > maior:
        print(receita)



def coluna_lista(nome_arquivo: str, indice_coluna: int):

    coluna = []

    with open(file= nome_arquivo, mode='r', encoding='utf8') as arquivo:
        linha = arquivo.readline()
        linha = arquivo.readline()
        while linha:
            linha_separada = linha.split(sep=',')
            coluna_separada = linha_separada[indice_coluna]
            coluna.append(coluna_separada)
            linha = arquivo.readline()
    
    return coluna


leu_com_sucesso = coluna_lista(r'C:\Users\Samsung\Desktop\Git- Estudo Python\Ler arquivos\CHATGPT.txt', 2)

print(leu_com_sucesso)