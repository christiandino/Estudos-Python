from datetime import date
class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self._data_nascimento = data_nascimento

    

    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days
    
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, value):
        if not isinstance(value, date):
            raise ValueError('data_nascimento deve ser um objeto do tipo date')
        self._data_nascimento = value


p1 = Pessoa('Christian', date(1996,2,7))
p1.data_nascimento = date(2000, 8, 1)
print(p1.dias_vividos())

#p1.data_nascimento = date(1996,2,8)
# p2 = Pessoa('Alan', date(2003, 3, 16))
# print(p2.dias_vividos())