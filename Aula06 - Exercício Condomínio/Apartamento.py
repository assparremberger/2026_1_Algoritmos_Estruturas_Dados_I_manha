from Torre import Torre
class Apartamento:

    def __init__(self, id = 0, numero = None, torre = Torre() ):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = None
        self.proximo = None
    
    def __str__(self):
        txt = "Apartamento: " + str(self.id)
        txt += "\nNúmero: " + self.numero
        txt += "\n" + str( self.torre )
        if self.vaga:
            txt += "\nVaga: " + str(self.vaga)
        else:
            txt += "\nVaga: Sem vaga de garagem"
        return txt
    
    def imprimir(self):
        print( self )