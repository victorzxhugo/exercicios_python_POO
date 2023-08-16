class Conta_bancaria:
    def __init__(self,numero:int, titular:str,saldo:float):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def deposito(self,valor):
        self.saldo += valor
        return print(f'Deposito no valor de {valor} realizado.')
    def printar_dados(self):
        print(f'\nTitular: {self.titular}\nNúmero; {self.numero}\nSaldo: {self.saldo}')



c1 =Conta_bancaria(100,'Victor',1000)
c1.printar_dados()
c1.deposito(122.45)
c1.printar_dados()
