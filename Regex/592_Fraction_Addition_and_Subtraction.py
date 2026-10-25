# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: re.findall recorre la cadena de longitud n para extraer los números y se usa espacio lineal para almacenar las fracciones resultantes.

import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Usamos expresiones regulares para encontrar todos los números con su signo (numerador y denominador)
        # Buscamos un opcional de signo seguido de dígitos, una diagonal y más dígitos
        numeros = re.findall(r'[+-]?\d+/\d+', expression)
        
        num_acum = 0
        den_acum = 1
        
        for frac in numeros:
            # Separamos el numerador y denominador de cada fracción
            n, d = map(int, frac.split('/'))
            
            # Suma de fracciones: a/b + c/d = (a*d + c*b) / (b*d)
            num_acum = num_acum * d + n * den_acum
            den_acum = den_acum * d
            
        # Función auxiliar para calcular el máximo común divisor (MCD) usando enteros
        def mcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)
            
        comun = mcd(num_acum, den_acum)
        
        # Simplificamos la fracción resultante
        num_acum //= comun
        den_acum //= comun
        
        return f"{num_acum}/{den_acum}"