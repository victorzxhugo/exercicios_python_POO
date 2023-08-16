class Passageiro:
    def __init__(self, nome:str, num_passaporte:str):
        self.nome = nome
        self.num_passaporte = num_passaporte

class Voo:
    def __init__(self, num_voo:str, origem:str, destino:str, capacidade_max:int):
        self.num_voo = num_voo
        self.origem = origem
        self.destino = destino
        self.capacidade_max = capacidade_max
        self.reservas = []

    def verificar_lotacao(self):
        return len(self.reservas) >= self.capacidade_max

    def reservar_assento(self,passageiro):
        if self.verificar_lotacao() is False:
            reservar = Reserva(passageiro,self)
            self.reservas.append(reservar)
        else:
            print(f'Voo {self.num_voo} lotado: {passageiro.nome} não foi reservado assento para você ')

    def listar_reservas(self):
        if len(self.reservas) == 0:
            print(f'\nVoo Nº: {self.num_voo}\nLista de passageiros:')
            print(f'O voo ainda não possui passageiros')
        else:
            print(f'\nVoo N º: {self.num_voo}\nLista de passageiros:')
            for i in self.reservas:
                print(f'Passageiro: {i.passageiro.nome}')

class Reserva:
    def __init__(self, passageiro, voo):
        self.passageiro = passageiro
        self.voo = voo

victor = Passageiro('Victor','123')
fernando = Passageiro('Fernando','321')
rafael = Passageiro('Rafael','123')
danilo = Passageiro('Danilo','321')

voo1 = Voo('0101','Floripa','Guarulhos',2)
voo2 = Voo('0202','Palhoça','São José',3)

voo1.reservar_assento(victor)
voo1.reservar_assento(fernando)
voo1.reservar_assento(rafael)

voo1.listar_reservas()
voo2.listar_reservas()

