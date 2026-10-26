# Complejidad temporal: O(n log n)
    # Complejidad espacial: O(n) (necesaria para almacenar el arreglo de intervalos fusionados y por el costo de ordenamiento)
    # Justificación: Se ordenan los intervalos basándose en su valor inicial, lo cual toma O(n log n). 
    # Posteriormente se recorren los n intervalos una sola vez en tiempo lineal O(n).
class Solution:
    
    def merge(self, intervals):
        if not intervals:
            return []
        
        # Ordenamos los intervalos por su punto de inicio
        intervals.sort(key=lambda x: x[0])
        
        fusionados = [intervals[0]]
        
        for actual in intervals[1:]:
            ultimo_fusionado = fusionados[-1]
            
        
            if actual[0] <= ultimo_fusionado[1]:
                # Fusionamos actualizando el valor máximo del fin
                ultimo_fusionado[1] = max(ultimo_fusionado[1], actual[1])
            else:
                # Si no se traslapan, lo agregamos como un nuevo intervalo independiente
                fusionados.append(actual)
                
        return fusionados
