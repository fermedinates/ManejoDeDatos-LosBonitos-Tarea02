# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: Se recorre la cadena una sola vez y la pila
# puede almacenar hasta n/2 símbolos de apertura.

class Solution:
    def isValid(self, s: str) -> bool:
        pila = []

        for caracter in s:
            if caracter == '(' or caracter == '[' or caracter == '{':
                pila.append(caracter)
            else:
                if not pila:
                    return False

                tope = pila.pop()

                if caracter == ')' and tope != '(':
                    return False
                if caracter == ']' and tope != '[':
                    return False
                if caracter == '}' and tope != '{':
                    return False

        return len(pila) == 0
