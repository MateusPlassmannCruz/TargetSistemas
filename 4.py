"""
Desafio 4 da selação de estágio Target Rotation
Autoria: Mateus Plassmann Cruz
Número: +55 (41) 98875-8311
Email: mpcruz@outlook.com
"""

prefix_list = [
    {"name": "sp","value": 67836.43},
    {"name": "rj","value": 36678.66},
    {"name": "mg","value": 29229.88},
    {"name": "es","value": 27165.48},
    {"name": "outros","value": 19849.53}
]


def percentage():
    values_list = [value['value'] for value in prefix_list]

    total = sum(values_list)

    for i in prefix_list:
        per = ((i['value']/total)*100)
        per = str(round(per, 2))
        name = i['name'].upper()
        print(f'[*] Percentual de reprensentação de {name} {per}%')

percentage()