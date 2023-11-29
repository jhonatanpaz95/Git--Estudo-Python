
class Animal():

    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def faz_som(self, som):
        self.som = som

    def Exibir_informacao(self):
        print(f'O animal é {self.nome}, tem {self.idade} anos, é um tipo de animal {self.tipo}')
        print(f'{self.nome} faz o som de {self.som}')


cachorro = Animal('cachorro', 15, 'terrestre/estimação')
cachorro.faz_som('(au au au)')
cachorro.Exibir_informacao()
