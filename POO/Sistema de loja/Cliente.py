class Cliente:
    
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.valor_total = 0
        self.lista_de_clientes = []

    def pagar_carrinho(self, carrinho):
        for prod in carrinho.lista_de_produtos:
            self.valor_total += prod['produto'].preco * prod['qtd_itens']

        if self.saldo >= self.valor_total:
            self.saldo -= self.valor_total
            return f'Parabéns pela compra, seu saldo atual agora é de: R$ {self.saldo:.2f}'
        else:
            return f'Saldo insuficiente. Sua compra deu: R$ {self.valor_total:.2f} e seu saldo é de: R$ {self.saldo:.2f}'

    # def pagar_carrinho(self, carrinho) -> bool:
    #     for prod in carrinho.lista_de_produtos:
    #         self.valor_total += prod['produto'].preco * prod['qtd_itens']

    #     if self.saldo >= self.valor_total:
    #         self.saldo -= self.valor_total
    #         return True
    #     else:
    #         return False

    
