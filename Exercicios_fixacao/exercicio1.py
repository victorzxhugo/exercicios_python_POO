class Produto:
    def __init__(self, nome:str ,preco:float, qtd_estoque:int):
        self.nome = nome
        self.preco = preco
        self.qtd_estoque = qtd_estoque

    def adicionar_estoque(self, qtd:int):
        self.qtd_estoque += qtd
        return print(f'Adicionou {qtd} {self.nome} do estoque')

    def remover_estoque(self, qtd:int):
        self.qtd_estoque -= qtd
        return print(f'Removeu {qtd} {self.nome} do estoque')

    def calcular_estoque(self):
        return self.preco * self.qtd_estoque


banana = Produto('Bananas',2.99,10)
maca = Produto('Maças',3.00,12)
pera = Produto('Peras',4.55,36)


banana.adicionar_estoque(10)
banana.remover_estoque(5)

print(f'Calculo estoque: {banana.calcular_estoque():.2f} reais')



