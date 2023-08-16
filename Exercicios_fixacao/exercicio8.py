class Sensor:
    def __init__(self,id:str,unidade_medida:str,temp_atual:float):
        self.id = id
        self.unidade_medida = unidade_medida
        self.temp_atual = temp_atual

    def atualizar_temp(self,temp:float):
        self.temp_atual = temp
        return print(f'Temperatura atualizada para {temp}')

    def printar_leitura(self):
        return print(f'Id: {self.id}\nUnidade de medida: {self.unidade_medida}\nTemperatura atual: {self.temp_atual}')


s1 = Sensor('1','ml',32)
s1.printar_leitura()
s1.atualizar_temp(45)
s1.printar_leitura()
