# Complejidad temporal: O(n)
# Complejidad espacial: O(k)
# Justificación: cada índice entra una vez al deque y sale una vez (por el frente
# o por el final), por lo que el total de operaciones es O(n). El deque guarda a
# lo más k índices, en orden decreciente de sus valores (cola monótona).

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # índices; nums[dq[0]] es el máximo de la ventana
        res = []
        for i, x in enumerate(nums):
            # Sale del frente el índice que ya quedó fuera de la ventana
            if dq and dq[0] <= i - k:
                dq.popleft()
            # Se descartan por atrás los menores o iguales a x: nunca serán máximo
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
