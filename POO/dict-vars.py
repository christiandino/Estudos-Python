class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    

dados = {'nome': 'Christian', 'idade': 28}
p1 = Pessoa(**dados)
# p1= Pessoa(idade=35, outra='coisa') a linha de cima de um modo diferente
p1 = Pessoa('Christian', 28)
#p2 = Pessoa('Allan', 21)

#p2.nome=('Eita')
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)

print(vars(p1))
print(p1.nome)
