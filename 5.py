"""
Desafio 5 da selação de estágio Target Rotation
Autoria: Mateus Plassmann Cruz
Número: +55 (41) 98875-8311
Email: mpcruz@outlook.com
"""

def recursion(s):
    if len(s) == 0:
        return s
    else: 
        return recursion(s[1:]) + s[0]
    
invert = input('[*] Digite a string a ser invertida: ')
print(recursion(invert))