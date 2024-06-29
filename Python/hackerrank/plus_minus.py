import math
import os
import random
import re
import sys

def statement():
    print('''
    Dado um array de inteiros, calcule as proporções de seus elementos que são 
    positivos, negativos e zero. Imprima o valor decimal de cada fração em uma
    nova linha com 6 casas decimais após o ponto. Nota: Este desafio introduz 
    problemas de precisão. Os casos de teste são ajustados para seis casas 
    decimais, embora respostas com erro absoluto de até 10^-4 sejam aceitáveis.
    Exemplo: arr = [1,1,0,-1,1] Existem N = 5 elementos, dois positivos, dois
    negativos e um zero. Suas proporções são 2/5 = 0.400000, 2/5 = 0.400000 e 
    1/5 = 0.200000. Os resultados são impressos como: 0.400000 0.400000 0.200000
    Descrição da Função: Complete a função plusMinus no editor abaixo. plusMinus
    em o(s) seguinte(s) parâmetro(s):int arr[n]: um array de inteiros.
    Imprima as proporções de valores positivos, negativos e zeros no array. 
    Cada valor deve ser impresso em uma linha separada com 6 dígitos após o ponto
    decimal. A função não deve retornar um valor. Formato de Entrada: A primeira 
    linha contém um inteiro, 'n', o tamanho do array. A segunda linha contém 'n'
    inteiros separados por espaço que descrevem arr[n].
    Restrições: 0 < n <= 100, -100 <= arr[i] <= 100. Formato de Saída: Imprima as 
    seguintes 3 linhas, cada uma com 6 casas decimais:
    proporção de valores positivos
    proporção de valores negativos
    proporção de zeros
    Entrada de Exemplo: 
    STDIN               Função 
    6                   tamanho do arr[] n = 6
    -4 3 -9 0 4 1       arr = [-4, 3, -9, 0, 4, 1]
    Saída de Exemplo:
    0.500000
    0.333333
    0.166667

    Explicação

    Há 3 números positivos, 2 números negativos e 1 zero no array.
    As proporções de ocorrência são positivas: 3/6 = 0.500000, negativas: 2/6 = 0.333333 e zeros: 1/6 = 0.166667.
''')

def plusMinus(arr):

    positivos, negativos, zeros = 0 
    n = len(arr)
    

if __name__ == '__main__':

    statement()

    n = int(input('Informe o tamanho do array: ').strip())

    arr = list(map(int, input("Insira o array: ").rstrip().split()))

resultado =  plusMinus(arr)
print('O resultado final é: ', resultado)