
class Aluno:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade
        self.disciplinas = []

    def adicionar_diciplinaas(self,disc:str):
        self.disciplinas.append(disc)
        return print(f'Disciplina {disc} adicionada com sucesso.')

    def mostrar_disciplinas(self):
        print(f'\nAluno - {self.nome}\nLista de matérias cursadas:\n-----')
        for i in self.disciplinas:
            print(i)
        print('-----')
victor = Aluno('Victor',23)

victor.adicionar_diciplinaas('Física')
victor.adicionar_diciplinaas('Matemática')
victor.adicionar_diciplinaas('Biologia')

victor.mostrar_disciplinas()



