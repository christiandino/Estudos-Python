from tabulate import tabulate
import pandas as pd
from Loja import Loja

class Carrinho:
    
    def __init__(self, loja):
        self.loja = loja
        self.lista_de_produtos = []


    def adicionar_item(self, produto, qtd_itens):
        existe = False
        for prod_loja in self.loja.prod_loja:
             # item carrinho       # produto na loja
            if prod_loja.produto == produto.produto:
                existe = True
        if not existe: raise Exception("Esse produto não existe na loja")
            
        if qtd_itens <= produto.qtd_estoque:
            # diminuindo o estoque da loja pela qtd_itens
            produto.qtd_estoque -= qtd_itens
            item = {'produto': produto, 'qtd_itens': qtd_itens}
        else:
            item = {'produto': produto, 'qtd_itens': produto.qtd_estoque}
            print(f'Não temos a quantidade de itens que você escolheu, temos apenas: {produto.qtd_estoque} {produto.produto}. Você pegou todos')
            produto.qtd_estoque = 0

        prod_repetido = False
        for prod in self.lista_de_produtos:
            if prod['produto'].produto == produto.produto:
                prod['qtd_itens'] = prod['qtd_itens'] + qtd_itens
                prod_repetido = True
                break
        
        if not prod_repetido:
            self.lista_de_produtos.append(item)

        if len(self.lista_de_produtos) == 0:
            self.lista_de_produtos.append(item)

    def devolver_estoque(self, produto, qtd_itens):
        existe = False
        for prod in self.lista_de_produtos:
            if prod['produto'].produto == produto.produto:
                existe = True           
            if qtd_itens > prod['qtd_itens']:
                raise Exception(f'Voce esta tentando tirar mais itens do que voce tem no carrinho')
            if prod['produto'].produto == produto.produto:
                produto.qtd_estoque += qtd_itens
                prod['qtd_itens'] -= qtd_itens
        for prod in self.lista_de_produtos:
            if prod['qtd_itens'] == 0:
                self.lista_de_produtos.remove(prod)
        if existe == False:
            raise Exception("Este item não está no seu carrinho para ser removido")           
                
            


    def listar_carrinho(self):
        df_table = pd.DataFrame([{'produto': item['produto'].produto, 'preco': item['produto'].preco, 'qtd_produto': item['qtd_itens']} for item in self.lista_de_produtos])
        tabela_formatada = tabulate(df_table, headers=['Id','Produto','Preço','Qtd produto'], tablefmt="pipe")
        return tabela_formatada











        
    # def devolver_estoque(self, produto, qtd_itens):
    #     encontrado_no_carrinho = False
    #     for prod in self.lista_de_produtos:
    #                 # item no carrinho    # item na loja
    #         if prod['produto'].produto == produto.produto:
    #             if qtd_itens <= prod['qtd_itens']:
    #                 # alterando o meu estoque
    #                 produto.qtd_estoque += qtd_itens
    #                 # alterando o meu carrinho
    #                 prod['qtd_itens'] -= qtd_itens

    #                 if prod['qtd_itens'] == 0:
    #                     self.lista_de_produtos.remove(prod)
    #                 encontrado_no_carrinho = True
    #             else:
    #                 raise Exception(f"Você está tentando devolver mais itens do que há no carrinho. Itens no carrinho: {prod['qtd_itens']}")
    #             break

    #     if not encontrado_no_carrinho:
    #         raise Exception("Esse produto não está no carrinho")