from Torre import Torre
from Apartamento import Apartamento
from Lista import Lista
from Fila import Fila

t1 = Torre( nome = "Torre A" , end = "Rua A" )
ap1 = Apartamento(1, "101" , t1)
ap1.vaga = 1
ap2 = Apartamento(2, "102" , t1)
ap2.vaga = 2
ap3 = Apartamento(3, "103" , t1)
ap3.vaga = 3
ap4 = Apartamento(4, "104" , t1)

lista = Lista()
lista.add( ap1 )
lista.add( ap2 )
lista.add( ap3 )

fila = Fila()
fila.add( ap4 )
op = -1

def menu():
    print(" --------------------------- ")
    print("| 1) Adicionar Apartamento  |")
    print("| 2) Liberar vaga           |")
    print("| 3) Imprimir Lista de APs  |")
    print("| 4) Imprimir Fila de APs   |")
    print("| 0) Sair                   |")
    print(" --------------------------- ")


def adicionar():
    id = int( input("Id do AP: ") )
    numero = input("Número do AP: ") 
    novoApp = Apartamento( id, numero , t1)
    fila.add( novoApp )

def liberarVaga( ):
    vaga = int( input("Qual vaga será liberada? ") )
    apPerdeuVaga = lista.remover( vaga )
    if apPerdeuVaga :
        apPerdeuVaga.proximo = None
        apPerdeuVaga.vaga = None
        fila.add( apPerdeuVaga )
        apGanhouVaga = fila.remover()
        if apGanhouVaga:
            apGanhouVaga.proximo = None
            apGanhouVaga.vaga = vaga
            lista.add( apGanhouVaga )



while op != 0:
    menu()
    op = int( input("Digite sua opção: ") )
    if op == 1:
        adicionar()
    if op == 2:
        liberarVaga()
    if op == 3:
        lista.imprimir()
    if op == 4:
        fila.imprimir()
    if op < 0 or op > 4:
        print( "Opção inválida!")
    if op == 0:
        print( "Bye-bye!")

