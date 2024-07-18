
def statement():
    print("""
    Você está coreografando um show de circo com vários animais. Para um ato, 
    você tem dois cangurus em uma linha numérica prontos para pular na direção 
    positiva (ou seja, em direção ao infinito positivo).

    O primeiro canguru começa na localização x1 e se move a uma taxa de v1 
    metros por salto. O segundo canguru começa na localização x2 e se move 
    a uma taxa de v2 metros por salto. Você tem que descobrir uma maneira de 
    fazer com que ambos os cangurus estejam na mesma localização ao mesmo 
    tempo como parte do show. Se for possível, retorne SIM, caso contrário, 
    retorne NÃO.

    Exemplo:
    x1 = 2
    v1 = 1
    x2 = 1
    v2 = 2

    Após um salto, ambos estão em x = 3, (x1 + v1 = 2 + 1, x2 + v2 = 1 + 2), 
    então a resposta é SIM.

    Descrição da Função
    Complete a função kangaroo abaixo.

    kangaroo tem os seguintes parâmetros:
    int x1, int v1: posição inicial e distância do salto para o canguru 1
    int x2, int v2: posição inicial e distância do salto para o canguru 2
    Retornos

    string: ou SIM ou NÃO

    Formato de Entrada

    Uma única linha de quatro inteiros separados por espaço que indicam os 
    valores respectivos de x1, v1, x2 e v2.

    Restrições
    0 <= x1 < x2 <= 10000
    1 <= v1 <= 10000
    1 <= v2 <= 10000

    Exemplo de Entrada 0
    0 3 4 2
          
    Exemplo de Saída 0
    SIM
 
    Explicação 0
    Os dois cangurus pulam através da seguinte sequência de locais:

    Na imagem, fica claro que os cangurus se encontram na mesma localização 
    (número 12 na linha numérica) após o mesmo número de saltos (4 saltos), 
    e imprimimos SIM.

    Exemplo de Entrada 1
    0 2 5 3

    Exemplo de Saída 1
    NÃO

    Explicação 1

    O segundo canguru tem uma localização inicial que está à frente 
    (mais à direita) da localização inicial do primeiro canguru (ou seja, 
    x2 > x1). Como o segundo canguru se move a uma taxa mais rápida 
    (significando v2 > v1) e já está à frente do primeiro canguru, o primeiro 
    canguru nunca será capaz de alcançá-lo. Portanto, imprimimos NÃO.
    """)



def kangaroo(x1, v1, x2, v2):

    # verificação para igualdade nas velocidades, mas posições iniciais diferentes
    if v1 == v2:
        if x1 == x2:
            return 'YES'
        else:
            return 'NO'
    
    # diferença inicial 
    difference_position = x1 - x2

    # diferença de velocidade
    difference_velocity = v2 - v1

    # verificação do possível encontro dos cangurus
    if  difference_position % difference_velocity == 0 and difference_position / difference_velocity > 0:
        return "YES"
    else: 
        return "NO"
    

#statement()
print(kangaroo(0, 3, 4, 5))

""" if __name__ == '__main__':


 first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
     """