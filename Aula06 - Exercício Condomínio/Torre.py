class Torre:

    def __init__(self, id = 0, nome = None, end = None):
        self.id = id
        self.nome = nome
        self.endereco = end

    def __str__(self):
        return f"""Torre: {self.id} - {self.nome}
Endereço: {self.endereco}"""
    
    def imprimir(self):
        print( self )

    def cadastrar(self):
        pass