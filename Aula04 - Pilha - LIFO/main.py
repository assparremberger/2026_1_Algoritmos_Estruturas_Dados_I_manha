from Pilha import Pilha

lifo = Pilha()

lifo.imprimir()

lifo.add("João")
lifo.add("Maria")
lifo.add("José")
lifo.remover()
lifo.add("Júlia")
lifo.remover()
lifo.remover()
lifo.remover()


## FUAQ implementa uma pilha de livro.
# Cada livro deverá conter o título, a quantidade de página e 
# o autor, sendo que o autor deverá conter nome, 
# e ano de nascimento.
# Implemente um método para adicionar livros na pilha,
# um método para imprimir a pilha de livros,
# um método para remover um livro da pilha 
# e um método que o usuário informa o nome do autor e 
# lhe é informado quantos livros tem na pilha com este autor