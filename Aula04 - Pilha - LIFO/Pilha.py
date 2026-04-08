from No import No

class Pilha:

    def __init__(self):
        self.topo = None

    def add(self, valor):
        nodo = No(valor)
        if self.topo is not None: 
            nodo.prox = self.topo
        self.topo = nodo
        self.imprimir()

    def remover(self):
        if self.topo is not None:
            self.topo = self.topo.prox
        self.imprimir()

    def imprimir(self):
        print("--------------------")
        if self.topo is None:
            print("\nPilha Vazia")
        else:
            print("\nPilha - LIFO")
            aux = self.topo
            while aux:
                print( aux.dado )
                aux = aux.prox
        print("--------------------")
    
    