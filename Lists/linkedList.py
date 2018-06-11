from Node import Node, linkedList


lista = linkedList()

nodo = Node(1)
lista.addToFront(nodo)
nodo = Node(2)
lista.addToFront(nodo)
nodo = Node(3)
lista.addToFront(nodo)
nodo = Node(4)
lista.addToFront(nodo)

lista.printList()
print(lista.getSize())
