 # Complejidad temporal: O(n)
    # Complejidad espacial: O(n)
    # Justificación: Se recorre la lista de números una sola vez. En el peor 
    # de los casos, se almacenan n elementos en el diccionario (hashtable) 
    # para realizar búsquedas en tiempo constante O(1).
class Solution:
   
    def twoSum(self, nums, target):
        vistos = {}
        
        for i, num in enumerate(nums):
            complemento = target - num
            
            # Si el complemento ya existe en el diccionario, encontramos la pareja
            if complemento in vistos:
                return [vistos[complemento], i]
            
            # Si no está, guardamos el número actual y su índice
            vistos[num] = i
            
        return []
