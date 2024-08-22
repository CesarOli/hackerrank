def statement():
    print("""
Dois crianças, Lily e Ron, querem dividir uma barra de chocolate. Cada quadrado
tem um número inteiro.

Lily decide dividir um segmento contíguo da barra selecionado de forma que:

1. O comprimento do segmento corresponda ao mês de nascimento de Ron, e,
2. A soma dos números nos quadrados seja igual ao dia do nascimento de Ron.

Determine quantas maneiras ela pode dividir o chocolate.

Exemplo:
s = [2, 2, 1, 3, 2]
d = 4
m = 2

Lily quer encontrar segmentos que somem ao dia de nascimento de Ron, d = 4,
com um comprimento igual ao mês de nascimento, m = 2. Nesse caso, existem dois
segmentos que atendem aos critérios: [2, 2] e [1, 3].

Descrição da Função

Complete a função `birthday` no editor abaixo.

A função `birthday` possui os seguintes parâmetros:
- `int s[n]`: os números em cada um dos quadrados de chocolate.
- `int d`: o dia do nascimento de Ron.
- `int m`: o mês de nascimento de Ron.

Retorno:
- `int`: o número de maneiras que a barra pode ser dividida.

Formato de Entrada:
- A primeira linha contém um número inteiro `n`, o número de quadrados na barra
de chocolate.
- A segunda linha contém `n` inteiros separados por espaço `s[i]`, os números
nos quadrados de chocolate onde `0 <= i < n`.
- A terceira linha contém dois inteiros separados por espaço, `d` e `m`, o dia
e o mês de nascimento de Ron.

Restrições:
- `1 <= n <= 100`
- `1 <= s[i] <= 5` onde `0 <= i < n`
- `1 <= d <= 31`
- `1 <= m <= 12`

Exemplo de Entrada 0:
5
1 2 1 3 2
3 2

Saída Esperada 0:
2

Explicação 0:
Lily quer dar a Ron `m = 2` quadrados que somem `d = 3`. Os dois segmentos que
atendem aos critérios são:

Exemplo de Entrada 1:
6
1 1 1 1 1 1
3 2

Saída Esperada 1:
0

Explicação 1:
Lily quer dar a Ron `m = 2` quadrados consecutivos de chocolate cujos inteiros
somem `d = 3`. Não há peças que satisfaçam esses critérios.

Portanto, imprimimos `0` como nossa resposta.

Exemplo de Entrada 2:
1
4
4 1

Saída Esperada 2:
1

Explicação 2:
Lily quer dar a Ron apenas um quadrado de chocolate com valor inteiro de `d = 4`.
Como o único quadrado de chocolate na barra satisfaz essa condição, imprimimos
`1` como nossa resposta.
""")

def birthday(s, d, m):
    for i in range(len(s) - m + 1):

        return
    if __name__ == '__main__':

        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        first_multiple_input = input().rstrip().split()

        d = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = birthday(s, d, m)
        