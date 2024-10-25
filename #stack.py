class Nodo:
    def __init__(self, dato):
        self.dato = dato  
        self.siguiente = None  


nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo1.siguiente = nodo2  

print(f"Nodo 1: {nodo1.dato}") 
print(f"Nodo 2: {nodo1.siguiente.dato}")  


###############################################3

class Queue:
    def __init__(self):
        self.items = []  

    def is_empty(self):
        return len(self.items) == 0  

    def enqueue(self, item):
        self.items.append(item)  

    def pull(self):
        if self.is_empty():
            print("La cola está vacía. No se puede retirar ningún elemento.")
            return None
        return self.items.pop(0)  

    def size(self):
        return len(self.items)  
    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]  



queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Elemento retirado:", queue.pull())  
print("Siguiente en la cola:", queue.peek())  
print("Tamaño actual:", queue.size())  


