class Carrinho_de_compras:

    def __init__(self):
        self.produtos_selecionados = []
        self.preco_correspondente = []

    def adicionar_produtos(self,produto:str,preco:float):
        self.produtos_selecionados.append(produto)
        self.preco_correspondente.append(preco)

    def calcular_total(self):
        total = sum( self.preco_correspondente)
        return print(f'-----\nTotal da compra: {total}\n-----')

    def mostrar_itens(self):
        print('Produtos no carrinho:\n----- ')
        for i in self.produtos_selecionados:
            print(i)



c1 = Carrinho_de_compras()

c1.adicionar_produtos('Arroz',10.99)
c1.adicionar_produtos('Abacate',8.56)
c1.adicionar_produtos('Farinha',4.88)

c1.calcular_total()
c1.mostrar_itens()


