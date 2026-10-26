# Complejidad temporal: O(n)
    # Complejidad espacial: O(n) (o O(1) si no contamos el arreglo de salida requerido)
    # Justificación: Se realizan dos recorridos  sobre el arreglo de tamaño n:
    #La lista resultado ocupa O(n) espacio
    #auxiliares O(1) espacio adicional 
class Solution:
    
    def productExceptSelf(self, nums):
        n = len(nums)
        resultado = [1] * n
        
        # 1. Pasada hacia la izquierda: calculamos el producto de todos los elementos a la izquierda
        prefijo = 1
        for i in range(n):
            resultado[i] = prefijo
            prefijo *= nums[i]
            
        # 2. Pasada hacia la derecha: multiplicamos por el producto de todos los elementos a la derecha
        sufijo = 1
        for i in range(n - 1, -1, -1):
            resultado[i] *= sufijo
            sufijo *= nums[i]
            
        return resultado
