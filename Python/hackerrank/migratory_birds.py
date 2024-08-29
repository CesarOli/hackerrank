def statement():
    print("""
Dado um array de avistamentos de pássaros onde cada elemento representa um 
tipo de pássaro, determine o id do tipo avistado com mais frequência. Se mais 
de um tipo tiver sido avistado o máximo de vezes, retorne o menor dos ids.

Exemplo
arr = [1, 1, 2, 2, 3]

Existem dois de cada dos tipos 1 e 2, e um avistamento do tipo 3. Escolha o 
menor dos dois tipos vistos duas vezes: tipo 1.

Descrição da Função

Complete a função migratoryBirds no editor abaixo.

migratoryBirds tem o(s) seguinte(s) parâmetro(s):

int arr[n]: os tipos de pássaros avistados
Retornos

int: o menor id do tipo de pássaro mais frequentemente avistado

Formato de Entrada

A primeira linha contém um número inteiro, n, o tamanho de arr.
A segunda linha descreve arr como n inteiros separados por espaço, cada um 
sendo um número de tipo do pássaro avistado.

Restrições
5 <= n <= 2 x 10 elevado a 5.
É garantido que cada tipo é 1, 2, 3, 4 ou 5.

Exemplo de Entrada 0

6
1 4 4 4 5 3

Exemplo de Saída 0

4

Explicação 0

Os diferentes tipos de pássaros ocorrem nas seguintes frequências:

Tipo 1: 1 pássaro
Tipo 2: 0 pássaros
Tipo 3: 1 pássaro
Tipo 4: 3 pássaros
Tipo 5: 1 pássaro

O número do tipo que ocorre com maior frequência é o tipo 4, portanto 
imprimimos 4 como nossa resposta.

Exemplo de Entrada 1

11
1 2 3 4 5 4 3 2 1 3 4

Exemplo de Saída 1

3

Explicação 1

Os diferentes tipos de pássaros ocorrem nas seguintes frequências:

Tipo 1: 2
Tipo 2: 2
Tipo 3: 3
Tipo 4: 3
Tipo 5: 1
Dois tipos têm uma frequência de 3, e o menor deles é o tipo 3.
""")


def migratoryBirds(arr):
    
    frequencias = {}
    
    for bird in arr:
        if bird in frequencias:
            frequencias[bird] += 1
        else:
            frequencias = 1
    return 


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    