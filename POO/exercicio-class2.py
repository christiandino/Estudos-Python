class Fabricante:
    def __init__(self, nome, cnpj, endereco, ramo:str):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.ramo = ramo # Carro Motor


    def listar_dados(self):
        texto =f'Nome do Fabricante: {self.nome}\n' \
               f'Nº do CNPJ: {self.cnpj}\n' \
               f'Endereço: {self.endereco}\n'
        
        if isinstance(self.ramo, str):
            ramo = f'Ramo: {self.ramo}'
        elif isinstance(self.ramo, (list, tuple)):  # Verifica se é uma lista ou tupla
            ramo = 'Ramo: ' + ', '.join(str(i) for i in self.ramo)
 
        return texto + ramo

    def criar_motor(self, nome, oleo, cilindradas, fabricante):
        if type(self.ramo) == str:
            if self.ramo.lower() in 'motor':
                return Motor(nome, oleo, cilindradas, fabricante)
            
        elif type(self.ramo) == list:
            for item in self.ramo:
                if item.lower() in 'motor': 
                    return Motor(nome, oleo, cilindradas, fabricante)
                
        raise Exception('O seu ramo não é de criação de motores.')


    
    def criar_carro(self, nome, marca, cor, ano, fabricante):
        if type(self.ramo) == str:
            print(type(self.ramo))
            if self.ramo.lower() in 'carro':
                return Carro(nome, marca, cor, ano, fabricante)
            
        elif type(self.ramo) == list:
            for item in self.ramo:
                if item.lower() in 'carro':  
                    return Carro(nome, marca, cor, ano, fabricante)
                
        raise Exception('O seu ramo não é de criação de carros.')

class Motor:
    def __init__(self, nome, oleo, cilindrada, fabricante):
        self.nome = nome
        self.oleo = oleo
        self.cilindrada = cilindrada
        self.fabricante = fabricante

    def listar_caracteristicas(self):
        return f'Nome do Motor: {self.nome}\n' \
               f'Nome do oleo: {self.oleo}\n' \
               f'Cilindrada: {self.cilindrada}\n'\
               f'Fabricante: {self.nome}'   



class Carro:
    def __init__(self, nome, marca, cor, ano, fabricante):
        self.nome = nome
        self.modelo = marca
        self.cor = cor
        self.ano = ano
        self.motor = None # objeto motor
        self.fabricante = fabricante # objeto fabricante
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, novo_motor):
        self._motor = novo_motor
    
    def listar(self):
        texto = f'<-- Carro -->\n'\
                f'Nome: {self.nome}\n'\
                f'Modelo: {self.modelo}\n'\
                f'Cor: {self.cor}\n'\
                f'Ano: {self.ano}\n\n'\
                f'<-- Fabricante do Carro -->\n'\
                f'{self.fabricante.listar_dados()}'\
                f'\n\n<-- Motor -->\n'\
                f'{self.motor.listar_caracteristicas()}\n\n'\
                f'<-- Fabricante do Motor -->\n'\
                f'{self.motor.fabricante.listar_dados()}'
        
        return texto

fabricante_chevrolet = Fabricante('Chevrolet', '654654651', 'Rua AFrÂnio', ['Motor', 'Carro'])
motor_ez4 = fabricante_chevrolet.criar_motor('Ez4', '4.0', '300', fabricante_chevrolet)
onix = fabricante_chevrolet.criar_carro('Onix', 'Chevrolet', 'Branco', '2023', fabricante_chevrolet)
onix.motor = motor_ez4
print(onix.listar())