from Livro import Livro

class Pilha:

    def __init__(self):
        self.topo = None

    def add(self, livro):
        if self.topo is not None: 
            livro.prox = self.topo
        self.topo = livro
        self.imprimir()

    def remover(self):
        if self.topo is not None:
            aux = self.topo
            self.topo = self.topo.prox
            del( aux )
        self.imprimir()

    def imprimir(self):
        print("--------------------")
        if self.topo is None:
            print("\nPilha de Livros Vazia")
        else:
            print("\nPilha de Livros ")
            aux = self.topo
            while aux:
                print( aux )
                aux = aux.prox
        print("--------------------")
    
    def contLivrosPorAutor(self, nome):
        if self.topo is not None:
            cont = 0
            aux = self.topo
            while aux:
                if nome == aux.autor.getNome() :
                    cont += 1
                aux = aux.prox
            if cont == 0:
                print( nome , " não possui livros na pilha!")
            else:
                print( nome , " possui ", cont, " livros na pilha")
