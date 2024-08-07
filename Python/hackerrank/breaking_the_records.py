 def statement():
    print('''
    Maria joga basquete universitário e quer se tornar profissional. Cada
    temporada, ela mantém um registro de seu desempenho. Ela contabiliza o
    número de vezes que quebra seu recorde de mais pontos e menos pontos em
    um jogo. Os pontos marcados no primeiro jogo estabelecem seu recorde para
    a temporada, e ela começa a contagem a partir daí.

    Exemplo:
    scores = [12, 24, 10, 24]

    As pontuações estão na mesma ordem dos jogos disputados. Ela contabiliza
    seus resultados da seguinte forma:

    | Jogo | Pontuação | Mínimo | Máximo | Min | Max |
    |------|------------|--------|--------|-----|-----|
    | 0    | 12         | 12     | 12     | 0   | 0   |
    | 1    | 24         | 12     | 24     | 0   | 1   |
    | 2    | 10         | 10     | 24     | 1   | 1   |
    | 3    | 24         | 10     | 24     | 1   | 1   |

    Dada as pontuações de uma temporada, determine o número de vezes que
    Maria quebra seus recordes de mais e menos pontos marcados durante a
    temporada.

    Descrição da Função

    Complete a função breakingRecords no editor abaixo.

    breakingRecords possui o(s) seguinte(s) parâmetro(s):

    - int scores[n]: pontos marcados por jogo

    Retorna

    - int[2]: Um array com o número de vezes que ela quebrou seus recordes. O
    índice 0 é para o recorde de mais pontos, e o índice 1 é para o recorde de
    menos pontos.

    Formato de Entrada

    A primeira linha contém um inteiro n, o número de jogos. A segunda linha
    contém n inteiros separados por espaço, descrevendo os valores respectivos
    de score0, score1, ..., score n-1.

    Restrições
    - 1 <= n <= 1000
    - 0 <= scores[i] <= 10^8

    Exemplo de Entrada 0

    9
    10 5 20 20 4 5 2 25 1

    Exemplo de Saída 0

    2 4

    Explicação 0

    O diagrama abaixo descreve o número de vezes que Maria quebrou seus
    melhores e piores recordes durante a temporada:

    Ela quebrou seu recorde de melhor pontuação duas vezes (após os jogos 2 e
    7) e seu recorde de pior pontuação quatro vezes (após os jogos 1, 4, 6 e
    8), então imprimimos 2 4 como nossa resposta. Note que ela não quebrou seu
    recorde de melhor pontuação durante o jogo 3, pois sua pontuação nesse
    jogo não foi estritamente maior do que seu recorde na época.

    Exemplo de Entrada 1

    10
    3 4 21 36 10 28 35 5 24 42

    Exemplo de Saída 1

    4 0

    Explicação 1

    O diagrama abaixo descreve o número de vezes que Maria quebrou seus
    melhores e piores recordes durante a temporada:

    Ela quebrou seu recorde de melhor pontuação quatro vezes (após os jogos 1,
    2, 3 e 9) e seu recorde de pior pontuação zero vezes (nenhuma pontuação
    durante a temporada foi menor do que a que ela obteve durante seu primeiro
    jogo), então imprimimos 4 0 como nossa resposta.
    ''')

def breakingRecords(scores):
    return
    
    
if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
