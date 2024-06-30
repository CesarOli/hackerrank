#!/bin/python3

import math
import os
import random
import re
import sys

def statement():
    print('''
Dado cinco inteiros positivos, encontre os valores mínimo e máximo que
podem ser calculados somando exatamente quatro dos cinco inteiros. Em
seguida, imprima os respectivos valores mínimo e máximo como uma única
linha com dois inteiros separados por espaço.

Exemplo:
arr = [1, 3, 5, 7, 9]

A soma mínima é: 1+3+5+7=16
e a soma máxima é 3+5+7+9=24. A função imprime 16 24.

Descrição da Função:

Complete a função miniMaxSum no editor abaixo.

miniMaxSum possui o(s) seguinte(s) parâmetro(s):

arr: um array de 5 inteiros.

Imprimir:

Imprima dois inteiros separados por espaço em uma linha: a soma mínima
e a soma máxima de 4 dos 5 elementos.

Formato de Entrada:

Uma única linha com cinco inteiros separados por espaço.

Restrições:
1 <= arr[i] <= 10**9

Formato de Saída:

Imprima dois inteiros separados por espaço denotando os respectivos
valores mínimo e máximo que podem ser calculados somando exatamente
quatro dos cinco inteiros. (A saída pode ser maior que um inteiro de
32 bits.)

Entrada de Exemplo:
1 2 3 4 5

Saída de Exemplo:
10 14

Explicação:

Os números são 1, 2, 3, 4 e 5. Calcule as seguintes somas usando quatro
dos cinco inteiros:

1. Some tudo, exceto 1, a soma é 2+3+4+5=14.
2. Some tudo, exceto 2, a soma é 1+3+4+5=13.
3. Some tudo, exceto 3, a soma é 1+2+4+5=12.
4. Some tudo, exceto 4, a soma é 1+2+3+5=11.
5. Some tudo, exceto 5, a soma é 1+2+3+4=10.

Dica: Cuidado com estouro de inteiros! Use um inteiro de 64 bits.
''')


def miniMaxSum(arr):

    total_soma = sum(arr)
    soma_min = total_soma - max(arr)
    soma_max = total_soma - min(arr)

    for num in arr:
        soma_atual = total_soma - num
        
        if soma_atual < soma_min:
            soma_min = soma_atual
        if soma_atual > soma_max:
            soma_max = soma_atual

    print(soma_min, soma_max)


if __name__ == '__main__':

    statement()

    arr = list(map(int, input('Insira os cinco (5) valores inteiros separados por espaço: ').rstrip().split()))

    miniMaxSum(arr)
