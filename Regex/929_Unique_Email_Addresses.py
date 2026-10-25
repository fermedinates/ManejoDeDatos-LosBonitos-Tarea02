# Complejidad temporal: O(n * m)
# Complejidad espacial: O(n * m)
# Justificación: Se recorren los n correos de longitud m procesando cada uno con expresiones regulares y guardándolos en un conjunto para filtrar duplicados.

import re

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        correos_unicos = set()
        
        for email in emails:
            # Separamos en local_name y domain_name usando el carácter @
            local_name, domain_name = email.split('@')
            
            # Cortamos todo lo que esté después del signo + en el local_name usando re.split
            local_name = re.split(r'\+', local_name)[0]
            
            # Quitamos todos los puntos . del local_name usando re.sub
            local_name = re.sub(r'\.', '', local_name)
            
            # Reconstruimos el correo limpio y lo agregamos al conjunto
            correo_limpio = f"{local_name}@{domain_name}"
            correos_unicos.add(correo_limpio)
            
        return len(correos_unicos)