class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_class(self):
        print('Classe PESSOA')
        print(self.nome, self.__class__.__name__)

class Cliente(Pessoa):
    def falar_nome_class(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'Aluno'


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_class()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_class()
print(a1.cpf)