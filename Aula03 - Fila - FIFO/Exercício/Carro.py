class Carro:

    def __init__(self, modelo = None, placa = None, ano = 2026):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.prox = None

    def __str__(self):
        txt =  "\nModelo: " + self.modelo 
        txt += "\nPlaca: " + self.placa
        txt += "\nAno: " + str(self.ano)
        return txt

        