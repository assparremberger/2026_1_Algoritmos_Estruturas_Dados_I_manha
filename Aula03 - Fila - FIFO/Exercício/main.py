from Carro import Carro
from Fila import Fila
fila = Fila()
op = -1
while op != 0:
    print( "1) Adicionar Carro" )
    print( "2) Imprimir Fila" )
    print( "3) Lavar carro" )
    print( "0) Sair" )
    op = int( input("Digite sua opção: ") )
    if op == 1:
        carro = Carro()
        carro.modelo = input("Modelo: ")
        carro.placa = input("Placa: ")
        carro.ano = int( input("Ano: ") )
        fila.add( carro )
    if op == 2:
        fila.imprimir()
    if op == 3:
        fila.lavar()  
    if op == 0:
        print( "Bye-bye!")
    if op > 3 or op < 0:
        print( "Opção inválida")