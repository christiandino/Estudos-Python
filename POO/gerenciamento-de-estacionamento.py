# Sistema de Gerenciamento de Estacionamento

class Veiculos:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

class Vagas:
    def __init__(self, qtd_vagas_maxima, status = True):
        self.qtd_vagas_maxima = qtd_vagas_maxima
        self.status = status # True para livre False para ocupado
        self.vagas_ocupadas = []

    def ocupar_vaga(self, veiculo):
        if self.status == True and len(self.vagas_ocupadas) < self.qtd_vagas_maxima:
            self.vagas_ocupadas.append(veiculo)
            print(f'O veiculo {veiculo.modelo} foi estacionado com sucesso')
        else:
            raise f'Sem vagas disponíveis'
    
    def procurar_veiculo(self, placa):
        for veiculo in self.vagas_ocupadas:
            if veiculo.placa == placa:
                return self.vagas_ocupadas.index(veiculo) 
        raise Exception(f"O veiculo com a placa: {placa} não se encontra estacionado")

    def liberar_vaga(self, placa):
        if len(self.vagas_ocupadas) <= 0:
            raise f'Não tem carros estacionados para liberar vaga'
        else:
            index_vaga = self.procurar_veiculo(placa)
            self.vagas_ocupadas.pop(index_vaga)
            return f'O veiculo da placa {placa} foi retirado do estacionamento'

    def listar_veiculos(self):
        print('LISTA DE VEÍCULOS ESTACIONADOS: ')
        for veiculo in self.vagas_ocupadas:
            print(f'{veiculo.modelo} {veiculo.marca} {veiculo.placa}')
    
        
vagas = Vagas(5)     
veiculo1 = Veiculos('FAL-0605', 'RENAULT', 'CLIO')
vagas.ocupar_vaga(veiculo1)
veiculo2 = Veiculos('GTM-8596', 'VOLKS', 'GOL G3')
vagas.ocupar_vaga(veiculo2)
veiculo3 = Veiculos('QKL-1910', 'MERCEDES', 'BMW')
vagas.ocupar_vaga(veiculo3)
veiculo4 = Veiculos('KGT', 'FIAT', 'UNO')
vagas.ocupar_vaga(veiculo4)
veiculo5 = Veiculos('TRU', 'CHEVROLET', 'ONIX')
vagas.ocupar_vaga(veiculo5)
# veiculo6 = Veiculos('UIU', 'CAPANGA', 'DEVIS') # raise f'Sem vagas disponíveis'
# vagas.ocupar_vaga(veiculo6)
print(vagas.liberar_vaga('\gsdfsdf'))










