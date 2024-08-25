def statement():
    print("""
Dado um array de inteiros e um inteiro positivo k, determine o número de pares
(i, j) onde i < j e ar[i] + ar[j] é divisível por k.

Exemplo:
ar = [1, 2, 3, 4, 5, 6]
k = 5
Três pares atendem aos critérios: [1, 4], [2, 3] e [4, 6].

Descrição da Função
Complete a função divisibleSumPairs no editor abaixo.
divisibleSumPairs tem os seguintes parâmetros:

int n: o comprimento do array ar
int ar[n]: um array de inteiros
int k: o divisor inteiro

Retorna
- int: o número de pares

Formato de Entrada
A primeira linha contém 2 inteiros separados por espaço, n e k.
A segunda linha contém n inteiros separados por espaço, cada um sendo um valor de ar[i].

Restrições
2 <= n <= 100
1 <= k <= 100
1 <= ar[i] <= 100

Exemplo de Entrada
STDIN           Função
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

Exemplo de Saída
5

Explicação

Aqui estão os 5 pares válidos quando k = 3:
(0, 2) -> ar[0] + ar[2] = 1 + 2 = 3
(0, 5) -> ar[0] + ar[5] = 1 + 2 = 3
(1, 3) -> ar[1] + ar[3] = 3 + 6 = 9
(2, 4) -> ar[2] + ar[4] = 2 + 1 = 3
(4, 5) -> ar[4] + ar[5] = 1 + 2 = 3
""")


def divisibleSumPairs(n, k, ar):
    
    count = 0

    for i in range(len(ar)):
    
    
            return count 

if __name__ == '__main__':

    statement()

    first_multiple_input = 0

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
