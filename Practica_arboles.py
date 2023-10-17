
class NodoARBOL:
    def __init__(self,dato = None):
        self.data = dato
        self.izquierdo = None
        self.derecho = None

raiz  = NodoARBOL()
raiz.data = "raiz"
raiz.izquierdo = NodoARBOL()
raiz.izquierdo.data = "perro"
raiz.derecho = NodoARBOL()
raiz.derecho.data = "gato"

print(raiz.izquierdo.data)