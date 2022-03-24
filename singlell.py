from multiprocessing.dummy import current_process
from os import remove


class SingleLL:
    class Node:
        def __init__(self,valor):
            self.value = valor
            self.next_node = None
    def __init__(self) :
        self.head = None
        self.tail = None
        self.lenght = 0
    '''Imprimir lista'''
    def show_nodes_list(self):
        node_list = []
        current_node = self.head
        while (current_node != None):
            node_list.append(current_node.value)
            current_node = current_node.next_node
        print(f"{node_list} Cantidad de nodos->{self.lenght}")
    '''Añadir nodo al inicio de la lista'''
    def prepend_node(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.lenght += 1
    '''Añadir nodo al final de la lista'''
    def append_node(self,value):
        new_node = self.Node(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.lenght += 1    
    '''Eliminar primer nodo de la lista'''
    def shift_node(self):
        if self.lenght == 0:
            self.head = None
            self.tail = None
        else:
            remove_node = self.head
            self.head = remove_node.next_node
            remove_node.next_node = None
            self.lenght -= 1
            print(f"El valor del nodo eliminado fue: {remove_node.value}")
    '''Eliminar ultimo nodo de la lista'''
    def pop_node(self):
        if self.lenght == 0:
            self.head = None
            self.tail = None
        else:
            current_node = self.head
            new_tail = current_node
            while(current_node.next_node != None):
                new_tail = current_node
                current_node = current_node.next_node
            self.tail = new_tail
            self.tail.next_node = None
            self.lenght -= 1
            print(f"El vallor del nodo eliminado fue: {current_node.value}")
    '''Consultar el valor de determinado nodo'''
    def get(self,index):
        if index == self.lenght:
            return self.tail
        elif index == 1:
            return self.head
        elif not(index >= self.lenght or index < 0):
            current_node = self.head
            contador = 1
            while (contador != index):
                current_node = current_node.next_node
                contador += 1
            return current_node
        else:
            print(f"El valor del indice consultado NO existe")
            return None
    '''Actualizar el valor de un nodo'''
    def update(self,value,index):
        nodo_objetivo = self.get(index)
        if nodo_objetivo != None:
            nodo_objetivo.value = value
        else:
            return None
    '''Añadir un nodo en una posicion especifica'''
    def insert(self,index,value):
        if index == self.lenght:
            return self.append_node(value)
        elif index == 1:
            return self.prepend_node(value)
        elif not(index > self.lenght or index < 1):
            new_node = self.Node(value)
            previous_node = self.get(index)
            nodos_siguientes = previous_node.next_node
            previous_node.next_node = new_node
            new_node.next_node = nodos_siguientes
            self.lenght += 1
        else:
            return None
    '''Eliminar nodo de una posicion especifica'''
    def remove(self,index):
        if index == 1:
            return self.shift_node()
        elif index == self.lenght:
            return self.pop_node
        elif not(index >= self.lenght or index < 1):
            nodos_anteriores = self.get(index-1)
            nodo_removido = nodos_anteriores.next_node
            nodos_anteriores.next_node = nodo_removido.next_node
            nodo_removido.next_node =  None
            self.lenght -= 1
            return nodo_removido
        else:
            return None
    '''Revertir una lista'''
    def reverse(self):
        reverse_node = None
        current_node = self.head
        self.tail = current_node
        while (current_node != None):
            next_node = current_node.next_node
            current_node.next_node = reverse_node
            reverse_node = current_node
            current_node = next_node
        self.head = reverse_node
        return self.head
    '''Vaciar lista'''
    def empty(self):
        self.head = None
        self.tail = None
        self.lenght = 0
    