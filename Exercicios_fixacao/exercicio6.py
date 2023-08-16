class Pedido:
    def __init__(self,numero:int, data:str):
        self.numero = numero
        self.data = data
        self.lista_itens = []

    def adicionar_itens(self,item:str):
        self.lista_itens.append(item)
        return print(f'Item "{item}" adicionado.')




p1 = Pedido(1,'15/08/2023')
p1.adicionar_itens('Abacate')

