from Torre import Torre
from Apartamento import Apartamento

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, ap):
        if self.inicio is None:
            self.inicio = ap
        else:
            self.fim.proximo = ap
        self.fim = ap

    def imprimir(self):
        print("\n\n-------------------")
        if self.inicio is None:
            print("Fila de Apartamentos vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux )
                aux = aux.proximo
                print("----------------------")

    def remover(self):
        if self.inicio is None:
            print( "\nNão há apartamentos fila" )
            return None
        else:
            aux = self.inicio
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            return aux