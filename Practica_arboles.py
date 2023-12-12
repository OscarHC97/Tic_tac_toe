
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


#__________________________________________________________________________________---------------____________

class Nodo:
    def __init__(self, valor, padre, es_raiz, es_izquierda, es_derecha) -> None:
        self.valor = valor
        self.izquierda =None
        self.derecha = None
        self.padre =  padre
        self.es_raiz = es_raiz
        self.es_izquierda = es_izquierda
        self.es_derecha  = es_derecha
        
     
        