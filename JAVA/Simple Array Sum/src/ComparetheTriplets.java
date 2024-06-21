import java.util.List;
import java.util.Scanner;
import java.util.ArrayList;


public class ComparetheTriplets {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        List<Integer> a = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            a.add(scanner.nextInt());
        }
        
        List<Integer> b = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            b.add(scanner.nextInt());
        }

        Statement();
        int [] resultado = comparetheTriplets(a, b);
        System.out.println("Alice: " + resultado[0] + ", Bob " + resultado[1] + ".");

        scanner.close();
    }
 
    public static void Statement() {
        System.out.println("""
\nAlice e Bob cada um criou um problema para o HackerRank. Um revisor avalia os
dois desafios, atribuindo pontos numa escala de 1 a 100 para três categorias:
clareza do problema, originalidade e dificuldade. A avaliação do desafio de Alice
é o triplo a = (a[0], a[1], a[2]), e a avaliação do desafio de Bob é o triplo 
b = (b[0], b[1], b[2]). A tarefa é encontrar seus pontos de comparação comparando 
a[0] com b[0], a[1] com b[1], e a[2] com b[2]. Se a[i] > b[i], Alice recebe 1 ponto.
Se a[i] < b[i], Bob recebe 1 ponto. Se a[i] = b[i], nenhuma pessoa recebe um ponto.
Os pontos de comparação são o total de pontos que uma pessoa ganhou.Dado a e b,
determine seus respectivos pontos de comparação.
Exemplo a = [1, 2, 3], b = [3, 2, 1]. Para os elementos 0, Bob recebe um ponto porque
a[0] < b[0]. Para os elementos iguais a[1] e b[1], nenhum ponto é ganho. Finalmente,
para os elementos 2, a[2] > b[2], então Alice recebe um ponto. O array de retorno é [1, 1]
com a pontuação de Alice primeiro e a de Bob em segundo. Descrição da Função. 
Complete a função compareTriplets no editor abaixo. compareTriplets tem os seguintes parâmetros:
int a[3]: avaliação do desafio de Alice int b[3]: avaliação do desafio de Bob Retorno int[2]:
A pontuação de Alice está na primeira posição e a de Bob na segunda. Formato de Entrada: 
A primeira linha contém 3 inteiros separados por espaço, a[0], a[1], e a[2], os respectivos valores no triplo a.
A segunda linha contém 3 inteiros separados por espaço, b[0], b[1], e b[2], os respectivos valores no triplo b.
Restrições 1 ≤ a[i] ≤ 100 1 ≤ b[i] ≤ 100 Exemplo de Entrada 0 5 6 7 3 6 10 Exemplo de Saída 0 
1 1
Explicação 0  Neste exemplo: Agora, vamos comparar cada pontuação individual:
5 > 3, então Alice recebe 1 ponto.
6 = 6, então ninguém recebe um ponto.
7 < 10, então Bob recebe 1 ponto.
A pontuação de comparação de Alice é 1 e a de Bob é 1. Portanto, retornamos o array [1, 1].
Exemplo de Entrada 1
17 28 30
99 16 8
Exemplo de Saída 1
2 1
Explicação 1
Comparando os elementos 0, 17 < 99, então Bob recebe um ponto.
Comparando os elementos 1 e 2, 28 > 16 e 30 > 8, então Alice recebe dois pontos.
O array de retorno é [2, 1].
""");

}
/*     }
    public static int[] comparetheTriplets() {
        int [] a = {17, 28, 30};
        int [] b = {99, 16, 8};

        int pointsAlice = 0;
        int pointsBob = 0;

        for (int i = 0; i < a.length; i++) {

            if (a[i] > b[i]) {
                pointsAlice++;
            
            } else if (a[i] < b[i]) {
                pointsBob++;

            }
        }
        int [] resultado = {pointsAlice, pointsBob};
        return resultado;
    } */
    public static int[] comparetheTriplets(List<Integer> a, List<Integer> b) {
        int pointsAlice = 0;
        int pointsBob = 0;

        for (int i = 0; i < a.size(); i++) {
            if (a.get(i) > b.get(i)) {
                 pointsAlice++;
            } else if (a.get(i) < b.get(i)) {
                pointsBob++;
            }
        }
        return new int[] {pointsAlice, pointsBob};
    }

}
    