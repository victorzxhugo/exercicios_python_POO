class Contato:

    def __init__(self, nome:str, telefone:str, email:str):
        self.nome = nome
        self.telefone = telefone
        self.email = email


    def atualizar_telefone(self, novo_tel:str):
        self.telefone = novo_tel


    def atualizar_email(self, novo_email:str):
        self.email = novo_email

    def printar_dados(self):
        return print(f'\nNome: {self.nome}\nTelefone: {self.telefone}\nEmail: {self.email}')



c1 =Contato('Victor','(48) 99605-4578','victor@gmail.com')


c1.printar_dados()

c1.atualizar_telefone('48 99605-4578')
c1.atualizar_email('novoemail@gmail.com')

c1.printar_dados()
