import math
import os
import random
import re
import sys

def statement():
    print('''
Você é responsável pelo bolo de aniversário de uma criança. Você decidiu
que o bolo terá uma vela para cada ano de idade dela. Eles só poderão apagar
as velas mais altas. Conte quantas velas são as mais altas.

Exemplo

candles = [4, 4, 1, 3]

As velas mais altas têm 4 unidades de altura. Existem 2 delas, então
retorne 2.

Descrição da Função

Complete a função `birthdayCakeCandles` no editor abaixo.

`birthdayCakeCandles` possui o(s) seguinte(s) parâmetro(s):

- `int candles[n]`: as alturas das velas

Retorna

- `int`: o número de velas que são as mais altas

Formato de Entrada

A primeira linha contém um único inteiro, `n`, o tamanho de `candles[]`.
A segunda linha contém `n` inteiros separados por espaço, onde cada
inteiro `i` descreve a altura de `candles[i]`.

Restrições

- 1 <= n <= 10^5
- 1 <= candles[i] <= 10^7

Entrada de Exemplo 0
4
3 2 1 3

Saída de Exemplo 0
2

Explicação 0
As alturas das velas são [3, 2, 1, 3]. As velas mais altas têm 3 unidades,
e existem 2 delas.
''')

""" # First Solution
def birthdayCakeCandles(candles):

    max_height = max(candles)

    count_max_height = candles.count(max_height)

    print(count_max_height) """


# Second Solution
def birthdayCakeCandles(candles):   
    max_height = candles[0]

    for height in candles:
        if height > max_height:
            max_height = height

    count_max_height = 0

    for height in candles:
        if height == max_height:
            count_max_height += 1

    return count_max_height

if __name__ == '__main__':

    statement()
    candles_count = int(input("informe o tamanho deste array: ").strip())

    candles = list(map(int, input('Informe os elementos deste array: ').rstrip().split()))

    result = birthdayCakeCandles(candles)
    
    print(result)