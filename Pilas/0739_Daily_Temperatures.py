# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: Se recorre la lista una vez y la pila puede almacenar n índices de días.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        respuesta = [0] * n
        pila = []

        for i in range(n):
            while pila and temperatures[i] > temperatures[pila[-1]]:
                dia = pila.pop()
                respuesta[dia] = i - dia

            pila.append(i)

        return respuesta
