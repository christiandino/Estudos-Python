from tabulate import tabulate
import pandas as pd
from datetime import datetime

class Cliente:
    
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.valor_total = 0
        self.produtos_comprados = []

    def pagar_carrinho(self, carrinho) -> bool:
        for prod in carrinho.lista_de_produtos:
            self.valor_total += prod['produto'].preco * prod['qtd_itens']

        if self.saldo >= self.valor_total:
            self.saldo -= self.valor_total
            self.produtos_comprados.append(carrinho.lista_de_produtos)
            self.__atualizar_carrinho(carrinho)
            return True, self.valor_total
        else:
            return False, 0
    



    def __atualizar_carrinho(self, carrinho):
        cliente = {
            'Nome':self.nome, 
            'Valor gasto':self.valor_total, 
            'Produtos':carrinho.lista_de_produtos,
            'Data de compra': datetime.now()
        }
        carrinho.loja._historico.append(cliente)
        carrinho.lista_de_produtos = []


        

    def listar_produtos_comprados(self):
        for carrinho in self.produtos_comprados:
            for produto in carrinho:
                #            objeto-produto   nome do produto
                return (produto['produto'].produto, produto['produto'].preco, produto['qtd_itens'])
