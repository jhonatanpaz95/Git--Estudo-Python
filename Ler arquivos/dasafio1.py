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

#print(media_idades)
#media_idades = sum(media_idades) / len(media_idades)
#print(media_idades)


receitas_monetarias = []

with open(file= r'C:\Users\Samsung\Desktop\Git- Estudo Python\Ler arquivos\CHATGPT.txt', mode='r', encoding='utf-8') as arquivo:
    arquivo.readline()
    linha = arquivo.readline()
    while linha:
        linha_separada = linha.split(sep=',')
        receita = linha_separada[3]
        receita = float(receita)
        receitas_monetarias.append(receita)
        linha = arquivo.readline()
    arquivo.close()

print(receitas_monetarias)

maior_receita = max(receitas_monetarias)
menor_receita = min(receitas_monetarias)

#for receita in receitas_monetarias:
    #if receita > maior_receita:
        #maior_receita = receita

print(f'a maior receita é R$ {maior_receita:.2f}')
print(f'a menor receita é R$ {menor_receita:.2f}')


score_credito = []
with open(file= r'C:\Users\Samsung\Desktop\Git- Estudo Python\Ler arquivos\CHATGPT.txt', mode='r', encoding='utf-8') as arquivo:
    arquivo.readline()
    linha = arquivo.readline()
    while linha:
        linha_separada = linha.split(sep=',')
        score = linha_separada[4]
        score = int(score)
        score_credito.append(score)
        linha = arquivo.readline()


menor_score = min(score_credito)
maior_score = max(score_credito)
media_score = sum(score_credito) / len(score_credito)
print(f'o maior score de credito é {maior_score}')
print(f'o menor score de credito é {menor_score}')
print(f'a média de score é {media_score}')


pessoas_maiores_30 = []
with open(file= r'C:\Users\Samsung\Desktop\Git- Estudo Python\Ler arquivos\CHATGPT.txt', mode='r', encoding='utf-8') as arquivo:
    linha = arquivo.readline()
    linha = arquivo.readline()
    while linha:
        linha_separada = linha.split(sep= ',')
        idade = linha_separada[1]
        idade = int(idade)
        if idade >= 30:
            pessoas_maiores_30.append(linha_separada)
        linha = arquivo.readline()
    
for pessoa in pessoas_maiores_30:
    print(pessoa)


ranking_score = []
indice = 0
with open(file= r'C:\Users\Samsung\Desktop\Git- Estudo Python\Ler arquivos\CHATGPT.txt', mode='r', encoding='utf-8') as arquivo:
    arquivo.readline()
    linha = arquivo.readline()
    while linha:
        linha_separada = linha.split(sep=',')
        score = linha_separada
        ranking_score.append(score)
        linha = arquivo.readline()

for linha in ranking_score:
    linha[4] = int(linha[4])
    top_1 = max(linha[4])
    print(top_1)