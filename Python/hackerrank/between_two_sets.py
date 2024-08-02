import os

def statement():
    print('''
        def statement():
    """
    Haverá dois arrays de inteiros. Determine todos os inteiros que satisfazem
    as seguintes duas condições:

    1. Os elementos do primeiro array são todos fatores do inteiro considerado.
    2. O inteiro considerado é um fator de todos os elementos do segundo array.

    Esses números são chamados de números entre os dois arrays. Determine quantos
    desses números existem.

    Exemplo:
    a = [2, 6]
    b = [24, 36]

    Existem dois números entre os arrays: 6 e 12.

    6 % 2 == 0, 6 % 6 == 0, 24 % 6 == 0, e 36 % 6 == 0 para o primeiro valor.
    12 % 2 == 0, 12 % 6 == 0, 24 % 12 == 0, e 36 % 12 == 0 para o segundo valor.
    Retorne 2.

    Descrição da Função:

    Complete a função getTotalX no editor abaixo. Ela deve retornar o número
    de inteiros que estão entre os conjuntos.

    getTotalX tem os seguintes parâmetros:

    int a[n]: um array de inteiros
    int b[m]: um array de inteiros

    Retornos:

    int: o número de inteiros que estão entre os conjuntos

    Formato de Entrada:

    A primeira linha contém dois inteiros separados por espaço, n e m, o número
    de elementos nos arrays a e b.

    A segunda linha contém n inteiros distintos separados por espaço, a[i] onde
    0 <= i < n.

    A terceira linha contém m inteiros distintos separados por espaço, b[i] onde
    0 <= j < m.

    Restrições:

    1 <= n, m <= 10
    1 <= a[i] <= 100
    1 <= b[j] <= 100

    Exemplo de Entrada:

    2 3
    2 4
    16 32 96

    Exemplo de Saída:

    3

    Explicação:

    2 e 4 dividem igualmente 4, 8, 12 e 16.
    4, 8 e 16 dividem igualmente 16, 32, 96.

    4, 8 e 16 são os únicos três números para os quais cada elemento de a é um
    fator e cada um é um fator de todos os elementos de b.
    """

def getTotalX(a, b):
    # Função ainda a ser implementada
    pass

if __name__ == '__main__':

    statement()

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    # Código para imprimir o resultado
    print(total)

          ''')
          
def getTotalX(a, b):
    return

if __name__ == '__main__':

    statement()

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
