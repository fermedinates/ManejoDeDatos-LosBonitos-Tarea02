# Complejidad temporal: O(1) en todas las operaciones
# Complejidad espacial: O(k)
# Justificación: se usa un arreglo fijo de tamaño k con un índice de cabeza y un
# contador de elementos; los índices se calculan con aritmética modular, sin
# recorrer ni desplazar elementos.

class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [0] * k
        self.k = k
        self.head = 0   # índice del frente
        self.size = 0   # número de elementos actuales

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[(self.head + self.size) % self.k] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[(self.head + self.size - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
