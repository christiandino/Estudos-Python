from tabulate import tabulate
import pandas as pd
from datetime import datetime

class Loja:

    def __init__(self):
        self.prod_loja = []
        self.numero_de_produtos = len(self.prod_loja)
        self.saldo_loja = 0
        self._historico = []

    @property
    def historico(self):
        return sorted(self._historico, key=lambda x: x['Nome'])
    
    @historico.setter
    def historico(self, value):
        self._historico = value

    

    def produtos_mais_vendidos(self):
        produtos_vendidos = {}

        for compra in self.historico:
            for item in compra['Produtos']:
                produto_nome = item['produto'].produto
                qtd_vendida = item['qtd_itens']

                if produto_nome in produtos_vendidos:
                    produtos_vendidos[produto_nome] += qtd_vendida
                else:
                    produtos_vendidos[produto_nome] = qtd_vendida

        produtos_ordenados = sorted(produtos_vendidos.items(), key=lambda x: x[1], reverse=True)


        print("Produtos mais vendidos:")
        for produto, quantidade in produtos_ordenados:
            print(f"{produto}: {quantidade} unidades")

    def listar_clientes(self):
        cliente_antigo = ''
        for i in self.historico:
            if cliente_antigo == i['Nome']:
                cliente ='' 
            else:
                cliente = f'Cliente: {i['Nome']}'

            print(cliente)




    def historico_de_compras(self):
        cliente_antigo = ''
        for i in self.historico:
            if cliente_antigo == i['Nome']:
                cliente ='' 
            else:
                cliente = f'Cliente: {i['Nome']}'
            cliente_antigo = i['Nome']
            print(cliente + f'\nValor gasto: R$ {i['Valor gasto']:.2f}\nData da Compra: {i['Data de compra']}\n')
            
            print('Produtos adquiridos do cliente')
            for k in i['Produtos']:
                print(f'Produto: {k['produto'].produto} - Preço: R$ {k['produto'].preco:.2f} - Qtd itens: {k['qtd_itens']}')
            print()

                 
    def adicionar_produto(self, produto):
        self.prod_loja.append(produto)


    def caixa(self, pago_ou_nao):
        pago, dinheiro = pago_ou_nao
        if pago: # pagou
            self.saldo_loja += dinheiro
            return True
        else: # não pagou
            return False
                 
            


    def remover_produto(self, nome_produto):
        for produto in self.prod_loja:
            if produto.produto == nome_produto:
                self.prod_loja.remove(produto)
                print(f'Produto "{nome_produto}" removido da loja.')
                return
        print(f'Produto "{nome_produto}" não encontrado na loja.')
        
    
    def listar_estoque(self):
        df_table = pd.DataFrame([{'produto': item.produto, 'preco': item.preco, 'qtd_produto': item.qtd_estoque} for item in self.prod_loja])
        tabela_formatada = tabulate(df_table, headers=['Id','Produto','Preço','Qtd produto'], tablefmt="pipe")
        return tabela_formatada