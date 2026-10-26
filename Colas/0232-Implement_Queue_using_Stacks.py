# Complejidad temporal: push O(1); pop y peek O(1) amortizado
# Complejidad espacial: O(n)
# Justificación: cada elemento pasa a lo más una vez de la pila de entrada a la de
# salida, así que el costo total de n operaciones es O(n), es decir O(1) amortizado
# por operación. Se guardan a lo más n elementos entre las dos pilas.

class MyQueue:

    def __init__(self):
        self.entrada = []  # pila donde se hace push
        self.salida = []   # pila de donde se hace pop/peek

    def push(self, x: int) -> None:
        self.entrada.append(x)

    def _pasar(self) -> None:
        # Solo se transfiere cuando la pila de salida está vacía
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())

    def pop(self) -> int:
        self._pasar()
        return self.salida.pop()

    def peek(self) -> int:
        self._pasar()
        return self.salida[-1]

    def empty(self) -> bool:
        return not self.entrada and not self.salida
