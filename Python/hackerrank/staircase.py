#!/bin/python3

import math
import os
import random
import re
import sys

def statement():
    print('''
Detalhes da Escada: 
Esta é uma escada de tamanho n = 4:

   #
  ##
 ###
####
Sua base e altura são ambas iguais a 'n'. Ela é desenhada usando símbolos # e espaços.
A última linha não é precedida por espaços. Escreva um programa que imprime uma escada
de tamanho 'n'. Descrição da Função: Complete a função `staircase` no editor abaixo.
`staircase` tem o(s) seguinte(s) parâmetro(s): int n: um número inteiro. 
Imprimir: Imprima uma escada conforme descrito acima.
Formato de Entrada: Um único número inteiro, 'n', indicando o tamanho da escada.
Restrições: 0 < n <= 100.
Formato de Saída: Imprima uma escada de tamanho 'n' usando símbolos # e espaços.
Nota: A última linha deve ter 0 espaços. Exemplo de Entrada: 6
Exemplo de Saída: 

     #
    ##
   ###
  ####
 #####
######
Explicação: A escada está alinhada à direita, composta por símbolos # e espaços,
e tem altura e largura de 'n = 6'.
''')

def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)

if __name__ == '__main__':
    statement()
    
    n = int(input('Informe o tamanho da escada: ').strip())

    staircase(n)
