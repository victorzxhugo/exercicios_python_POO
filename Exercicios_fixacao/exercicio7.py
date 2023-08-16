class Tarefa:
    def __init__(self,descricao:str,data_criacao:str,status=False):
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.status = status

    def marcar_concluida(self):
        self.status = True
        print('\nTarefa marcada como concluida\n')

    def printar_detalhes(self):
        status_str = "Concluída" if self.status else "Pendente"
        print(f'\nDescrição: {self.descricao}\nData de criação:{self.data_criacao} \nTarefa: {status_str}')


t1 = Tarefa('Tarefa POO','15/08/2023')
t1.marcar_concluida()
t1.printar_detalhes()
