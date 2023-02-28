"""
Desafio 3 da selação de estágio Target Rotation
Autoria: Mateus Plassmann Cruz
Número: +55 (41) 98875-8311
Email: mpcruz@outlook.com
"""

import json

def open_json():
    with open('dados.json', 'r') as file:
        return json.load(file)
    

def max_min_value():
    values = open_json()

    values_list = [value for value in values if value['valor'] != 0.0]

    min = values_list[0]['valor']
    max = values_list[0]['valor']

    for i in range(len(values_list)):
        if values_list[i]['valor'] < min:
            min = values_list[i]['valor']
            less_day = values_list[i]['dia']

        if values_list[i]['valor'] > max:
            max = values_list[i]['valor']
            more_day = values_list[i]['dia']

    print(f'[-] Dia {less_day} com {min} reais ocorreu o menor valor de faturamento... ')
    print(f'[+] Dia {more_day} com {max} reais ocorreu o maior valor de faturamento... ')


def average():
    values = open_json()

    values_list = [value['valor'] for value in values if value['valor'] != 0.0]

    avg = sum(values_list)/len(values_list)

    above_average = [value['dia'] for value in values if avg < value['valor']]

    above_average_days = len(above_average)

    print(f'[*] {above_average_days} dias {above_average} faturaram acima da média... ')

max_min_value()
average()