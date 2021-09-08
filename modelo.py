class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_likes(self):
        self.__likes += 1

    # define uma representação textual para o objeto
    def __str__(self):
        return f"{self.__nome} - {self.ano} - {self.__likes} likes"

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao} min - {self.likes} likes"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes"

class Playlist:
    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas

    @property
    def listagem(self):
        return self.__programas

    @property
    def tamanho(self):
        return len(self.__programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
todo_mundo_em_panico = Filme("Todo mundo em pânico", 1999, 100)
demolidor =  Serie('Demolidor', 2016, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()

todo_mundo_em_panico.dar_likes()
todo_mundo_em_panico.dar_likes()

demolidor.dar_likes()

vingadores.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, todo_mundo_em_panico]
playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

print(demolidor in playlist_fim_de_semana)