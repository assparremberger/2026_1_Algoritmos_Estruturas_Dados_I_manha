from Torre import Torre
from Apartamento import Apartamento

class Lista:

    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print("------------------")
        print("Lista de Apartamentos por ordem da vaga")
        if self.inicio is None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux )
                aux = aux.proximo
                print("----------------------")

    def add(self, ap:Apartamento):
        
        if self.inicio == None:
            self.inicio = ap
        else:
            if ap.vaga < self.inicio.vaga:
                ap.proximo = self.inicio
                self.inicio = ap
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if ap.vaga < aux.vaga:
                        ap.proximo = aux
                        ant.proximo = ap
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None:
                    ant.proximo = ap
        print( "Apartamento ", ap.numero, " adicionado na Lista")

    def remover(self, vaga):
        apRemovido = None
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            if vaga == self.inicio.vaga:
                apRemovido = self.inicio
                self.inicio = self.inicio.proximo 
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if vaga == aux.vaga:
                        apRemovido = aux
                        ant.proximo = aux.proximo
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
            if apRemovido:
                print("Apartamento ", apRemovido.numero , " removido!")
            else:
                print( vaga , " não encontrada!")
                
        return apRemovido
            


        
        