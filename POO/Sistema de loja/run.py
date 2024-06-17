from Cliente import Cliente
from Loja import Loja
from Produto import Produto
from Carrinho import Carrinho

# Criando loja
loja1 = Loja()

# Criando produtos
tenis_nike_shox = Produto('Nike Shox', 220.45, 50)
tenis_adidas_ultraboost = Produto('Super Star XLG', 150.75, 50)
tenis_puma_suede = Produto('Puma Suede', 250.80, 103)

# Adicionando produtos à loja
loja1.adicionar_produto(tenis_nike_shox)
loja1.adicionar_produto(tenis_adidas_ultraboost)
loja1.adicionar_produto(tenis_puma_suede)

carrinho = Carrinho(loja1)
carrinho.adicionar_item(tenis_nike_shox, 5)
carrinho.adicionar_item(tenis_adidas_ultraboost, 5)
carrinho.adicionar_item(tenis_puma_suede, 3)

carrinho2 = Carrinho(loja1)
carrinho2.adicionar_item(tenis_nike_shox, 1)
carrinho2.adicionar_item(tenis_adidas_ultraboost, 8)
carrinho2.adicionar_item(tenis_puma_suede, 1)

christian = Cliente('Christian', 10000)
Alan = Cliente('Alan', 10000)

loja1.caixa(christian.pagar_carrinho(carrinho))
loja1.caixa(Alan.pagar_carrinho(carrinho2))

loja1.historico_de_compras()