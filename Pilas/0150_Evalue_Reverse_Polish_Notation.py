# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: Se recorre la lista una sola vez y la pila puede almacenar n elementos.

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pila = []

        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                b = pila.pop()
                a = pila.pop()

                if token == "+":
                    pila.append(a + b)
                elif token == "-":
                    pila.append(a - b)
                elif token == "*":
                    pila.append(a * b)
                else:
                    resultado = int(a / b)
                    pila.append(resultado)

            else:
                pila.append(int(token))

        return pila.pop()
