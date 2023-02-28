"""
Desafio 2 da selação de estágio Target Rotation
Autoria: Mateus Plassmann Cruz
Número: +55 (41) 98875-8311
Email: mpcruz@outlook.com
"""

n = int(input('[*] Informe um número: '))

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


def check_fibonacci(fibonacci_list):
    if n not in fibonacci_list:
        print(f'[-] Número {n} não pertence a sequência Fibonacci! ')
    else:
        print(f'[+] Número {n} pertence a sequência Fibonacci! ')

gen = fibonacci(n)

fibonacci_list = list(fibonacci(n))
print(fibonacci_list)
check_fibonacci(fibonacci_list)
