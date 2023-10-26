# tudo sobre funções:

funcao = 'funções em python são definidas com a palavra reservada def():'
funcao += '\n' + 'elas podem receber ou não algum parametro Ex: def nome_da_função(parametro1: int, parametro2: int)'
funcao += '\nPossuem o return que é o valor que a função produz, quando não especificado o tipo de retorno é none.'
#print(funcao)

# exemplo de uma função def

def soma(numero1: int, numero2: int) -> int:
    resultado = numero1 + numero2
    print(f'o resultado da operação é {resultado}')
    return resultado

#soma(5,6)

# no caso acima sou obrigado a passar dois parametro inteiro
# se eu passar algum outro tipo de valor ou não passar outro parametro o meu codigo vai gerar uma excessão:
# pra resolver isso eu posso passar o parametro como obrigatório no caso de nao te argumento e tratar as excessões:

def nova_soma(numero1= 0, numero2 = 0) -> int:
    ''' programa recebe dois numeros e retorna a soma deles.
        só será feito a soma se for numeros inteiro, em caso de outro valor, etra na excessão
    '''
    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        resultado = numero1 + numero2
        print(f'o resultado da soma é: {resultado}')
        return resultado
    except ValueError:
        print('Erro: Certifique-se de inserir números inteiros válidos.')

nova_soma(10, 'abc')




