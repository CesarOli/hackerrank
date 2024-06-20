/* public class SolveMeFirst {
  
    public static int solveMeFirst(int a, int b) {
        
        int c = a + b;
        
        return c;
    }
    public static void main(String[] args) {
        int resultado = solveMeFirst(2, 3);
        System.out.println(resultado);
        
    }
} */


import java.util.*;

public class Solution {

    public static int solveMeFirst(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = scanner.nextInt();
        int b = scanner.nextInt();

        int resultado = solveMeFirst(a, b);

        System.out.println(resultado);

        scanner.close();
    }
}
