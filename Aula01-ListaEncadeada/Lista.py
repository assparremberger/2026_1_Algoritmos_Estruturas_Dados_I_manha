from No import No

class Lista:

    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print("------------------")
        print("Lista Encadeada por ordem de chegada")
        if self.inicio is None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox

    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()

        