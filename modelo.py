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

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)
