from Cliente import Cliente
from Loja import Loja
from Produto import Produto
from Carrinho import Carrinho

# Criando loja
loja1 = Loja()

# Criando produtos
tenis_nike_shox = Produto('Nike Shox', 220.45, 3)
tenis_adidas_ultraboost = Produto('Super Star XLG', 150.75, 3)
tenis_puma_suede = Produto('Puma Suede', 250.80, 3)

# Adicionando produtos à loja
loja1.adicionar_produto(tenis_nike_shox)
loja1.adicionar_produto(tenis_adidas_ultraboost)
loja1.adicionar_produto(tenis_puma_suede)
print("Lista do estoque")
print(loja1.listar_estoque())
carrinho = Carrinho(loja1)
carrinho.adicionar_item(tenis_nike_shox, 2)
carrinho.adicionar_item(tenis_adidas_ultraboost, 2)
carrinho.adicionar_item(tenis_puma_suede, 2)
print()
print('Lista do carrinho')
print(carrinho.listar_carrinho())
print()
print("Lista do estoque")
print(loja1.listar_estoque())
print()
print("Lista do estoque após cliente devolver item")
carrinho.devolver_estoque(tenis_nike_shox, 1)
print(loja1.listar_estoque())
print()
print('Lista do carrinho após o cliente ter devolvido o item')
print(carrinho.listar_carrinho())
print()
print()
print()
christian = Cliente('Christian', 2000)
print(christian.pagar_carrinho(carrinho))
# christian = Cliente.adicionar_cliente('Christian', 2000)
# alan = Cliente.adicionar_cliente('Alan', 1500)
# douglas = Cliente.adicionar_cliente('Douglas', 1400)
#print(christian.pagar_carrinho(carrinho))
#print('Lista de Clientes')
#(listar_clientes())



