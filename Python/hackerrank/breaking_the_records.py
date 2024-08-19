def statement():
    print("""
Desafio: Breaking Records

Maria adora basquete e mantém o registro de seus pontos em todos os jogos da
temporada. Ela quer saber quantas vezes quebrou seu recorde de pontos mais
altos e quantas vezes quebrou seu recorde de pontos mais baixos durante a
temporada. Isso é feito comparando o número de pontos de cada jogo com seus
recordes atuais de pontos mais altos e mais baixos.

Função:
A função breakingRecords deve calcular o número de vezes que Maria quebra seus
recordes de pontos mais altos e baixos. A função deve retornar uma lista de
dois inteiros. O primeiro inteiro é o número de vezes que ela quebrou seu
recorde de pontos mais altos durante a temporada e o segundo inteiro é o
número de vezes que ela quebrou seu recorde de pontos mais baixos.

Parâmetros:
- scores (list of integers): Uma lista de inteiros representando os pontos
  marcados por Maria em cada jogo.

Retorno:
- list of integers: Uma lista contendo dois inteiros, o primeiro é o número de
  vezes que Maria quebrou seu recorde de pontos mais altos e o segundo é o
  número de vezes que ela quebrou seu recorde de pontos mais baixos.

Exemplo:
- Entrada: scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
- Saída: [2, 4]
Explicação: Maria jogou 9 jogos. Seus recordes foram:
* Jogo 1 (10): Mais alto = 10, Mais baixo = 10
* Jogo 2 (5): Mais alto = 10, Mais baixo = 5 (1 recorde mais baixo)
* Jogo 3 (20): Mais alto = 20 (1 recorde mais alto), Mais baixo = 5
* Jogo 4 (20): Mais alto = 20, Mais baixo = 5
* Jogo 5 (4): Mais alto = 20, Mais baixo = 4 (2 recordes mais baixos)
* Jogo 6 (5): Mais alto = 20, Mais baixo = 4
* Jogo 7 (2): Mais alto = 20, Mais baixo = 2 (3 recordes mais baixos)
* Jogo 8 (25): Mais alto = 25 (2 recordes mais altos), Mais baixo = 2
* Jogo 9 (1): Mais alto = 25, Mais baixo = 1 (4 recordes mais baixos)

""")

def breakingRecords(scores):
    
    maximo_score = scores[0]
    minimo_score = scores[0]
    maximo_breaks = 0
    minimo_breaks = 0

    for score in scores[1:]:
        if score > maximo_score:
            maximo_score = score
            maximo_breaks += 1
        elif score < minimo_score:
            minimo_score = score
            minimo_breaks += 1

    return [maximo_breaks, minimo_breaks]

if __name__ == '__main__':

    statement()

    n = int(input('Diga o número de jogos realizados: ').strip())
    scores = list(map(int, input('Informe o total de pontos feitos em cada jogo, separado por um único espaço: ').rstrip().split()))

    result = breakingRecords(scores)
    print(f'Resultado: {result}')
