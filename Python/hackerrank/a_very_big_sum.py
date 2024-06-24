import math
import os
import random
import re
import sys

def statement():
    print('''
    Neste desafio, você precisa calcular e imprimir a soma dos elementos em um
    array, lembrando que alguns desses inteiros podem ser bastante grandes. 
    Descrição da Função: Complete a função aVeryBigSum no editor abaixo. Ela
    deve retornar a soma de todos os elementos do array. aVeryBigSum possui o(s)
    seguinte(s) parâmetro(s): int ar[n]: um array de inteiros. Retorno long: a
    soma de todos os elementos do array. Formato da Entrada: A primeira linha da
    entrada consiste em um inteiro. A próxima linha contém inteiros separados por
    espaço contidos no array. Formato da Saída: Retorne a soma inteira dos elementos
    no array. Restrições 1 <= n <= 10 0 <= ar[i] <= 10**10: Exemplo de Entrada: 5 
    1000000001 1000000002 1000000003 1000000004 1000000005. Saída 5000000015
''')

def aVeryBigSum(ar):
    soma = 0

    for i in ar:
        soma += i

    return soma

if __name__ == '__main__':
    statement()
    n = int(input('Digite a quantidade de elementos no array: ').strip())

    ar = list(map(int, input('Digite os elementos do array separados por espaço: ').strip().split()))
    
    resultado = aVeryBigSum(ar)
    
    print('A soma dos elementos do array é:', resultado)
