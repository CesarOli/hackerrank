#!/bin/python3

import math
import os
import random
import re
import sys

def statement():
    print('''
    Dada uma matriz quadrada, calcule a diferença absoluta entre as somas de 
    suas diagonais. Por exemplo, a matriz quadrada mostrada abaixo: 
    1 2 3 
    4 5 6 
    9 8 9
    A diagonal da esquerda para a direita = 1+5+9=15. A diagonal da direita para a 
    esquerda = 3+5+9=17. A diferença absoluta entre elas é 15-17=2.
          
    Descrição da função: Complete a função diagonalDifference no editor abaixo.
    diagonalDifference recebe o seguinte parâmetro: int arr[n][m]: uma matriz de 
    inteiros. Retorno: int: a diferença absoluta das diagonais. Formato de Entrada: 
    A primeira linha contém um único inteiro, 'n', o número de linhas e colunas na
    matriz quadrada 'arr'. Cada uma das próximas 'n' linhas descreve uma linha, 'arr[i]', e
    consiste em 'n' inteiros separados por espaço arr[i][j].
    Restrições: -100 <= arr[i][j]
    Formato de Saída: Retorne a diferença absoluta entre as somas das duas diagonais
    da matriz como um único inteiro. Exemplo de Entrada: 
    3
    11 2 4
    4 5 6
    10 8 -12
    Exemplo de Saída: 15
    Explicação: A diagonal principal é:
    11
        5
            -12
    Soma na diagonal principal: 11 + 5 - 12 = 4
    A diagonal secundária é:
          4
        5  
    10
    Soma na diagonal secundária: 4 + 5 + 10 = 19
    Diferença: |4 - 19| = 15
    Nota: |x| é o valor absoluto de x.
    ''')

def diagonalDifference(arr):

    #determinando o tamanho da matriz(Coluna x Linha)
    n = len(arr)

    #inicialização variaveis soma das diagonais
    soma_diagonal_esquerda_para_direita = 0
    soma_diagonal_direita_para_esquerda = 0
    
    #loop de iteração para inserir elementos nas variáveis soma diagonais
    for i in range (n):
        soma_diagonal_esquerda_para_direita += arr[i][i]
        soma_diagonal_direita_para_esquerda += arr[i][n - i - 1]
    
    #calculo da diferença absoluta
    diferenca_absoluta = abs(soma_diagonal_direita_para_esquerda - soma_diagonal_esquerda_para_direita)
    return diferenca_absoluta


if __name__ == '__main__':
    print('\nENUNCIADO\n')
    statement()

    #leitura dos valores do array
    n = int(input('Digite o numero de linhas e colunas da matriz: '))
    
    #alimentando o array com números fornecidos na leitura
    arr = []

    #loop resposável pela construção da matriz
    for _ in range(n):
        linha = list(map(int, input().split()))
        arr.append(linha)

    #atribuindo o resultado da função a variável resultado
    resultado = diagonalDifference(arr)

    print('A soma dos elementos na diagonal do array fornecido é: ', resultado)
