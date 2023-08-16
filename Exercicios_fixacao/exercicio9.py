class Livro:
    def __init__(self, título:str, autor:str, ano_de_publicacao:int, gênero:str):
        self.título = título
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.gênero = gênero

    def atualizar_ano_de_publicação(self, novo_ano):
        self.ano_de_publicacao = novo_ano

    def exibir_detalhes(self):
        print(f"Título: {self.título}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_de_publicacao}")
        print(f"Gênero: {self.gênero}")


livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, "Romance")
livro1.exibir_detalhes()

print("\nAtualizando ano de publicação...")
livro1.atualizar_ano_de_publicação(1889)
livro1.exibir_detalhes()
