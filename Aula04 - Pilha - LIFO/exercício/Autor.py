class Autor:

    def __init__(self, nome = "Sem nome", ano = 2020):
        self._nome = nome
        self.__ano = ano

    def setNome(self, valor):
        if valor != "" and valor != "Adalto":
            self._nome = valor

    def getNome(self):
        return self._nome
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        if valor < 2026:
            self.__ano = valor

    def __str__(self):
        txt = "Autor: " + self._nome
        txt += " - Ano: " + str( self.__ano )
        return txt
    
