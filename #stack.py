class Nodo:
    def __init__(self, dato):
        self.dato = dato  
        self.siguiente = None  


nodo1 = Nodo(10)
nodo2 = Nodo(20)
nodo1.siguiente = nodo2  

print(f"Nodo 1: {nodo1.dato}") 
print(f"Nodo 2: {nodo1.siguiente.dato}")  

