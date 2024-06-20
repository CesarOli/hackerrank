
public class SimpleArraySum {
    public static void main(String[] args) throws Exception {
        Enunciado();
        int ar [] = {1, 2, 3, 4, 10, 11};
        int finalSum = simpleArraySum(ar);
        System.out.println("A soma total dos elementos da lista é de " + finalSum + ".");
    }
    public static void Enunciado() {
        System.out.println("""
                \nDado um array de inteiros, encontre a soma de seus elementos.
                Por exemplo, se o array for ar = [1,2,3].1+2+3 = 6, entao retorne o 6.
                Descrição da Função. Complete a função simpleArraySum no editor abaixo.
                Ela deve retornar a soma dos elementos do array como um inteiro. 
                simpleArraySum tem os seguintes parâmetros: ar: um array de 
                inteiros. Formato de Entrada, a primeira linha contém um inteiro n
                ,n , indicando o tamanho do array.A segunda linha contém inteiros
                separados por espaço representando os elementos do array.
                Restrições: Formato de Saída: Imprima a soma dos elementos do 
                array como um único inteiro. Entrada de Exemplo: 1 2 3 4 10 11
                Saída de Exemplo: 31. Explicação: Imprimimos a soma dos elementos
                do array: 1+2+3+4+10+11=31\n"
                """);
    }
    
    public static int simpleArraySum(int[] ar) {
        int sum = 0;
        
        for (int num : ar){
            sum += num;
        }
        return sum;
    }
}
