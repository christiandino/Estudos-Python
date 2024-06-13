import datetime as dt

class Pessoa:
    ano = 2030

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = int(dt.datetime.now().year)

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    
p1 = Pessoa('Christian', 28)
p2 = Pessoa('Allan', 21)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

