# Complejidad temporal: O(n)
# Complejidad espacial: O(1)
# Justificación: re.fullmatch recorre la cadena de longitud n una sola vez y utiliza espacio auxiliar constante.

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Validamos con una expresión regular estándar para enteros, decimales y notación científica
        patron = r"^[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?$"
        return bool(re.fullmatch(patron, s))