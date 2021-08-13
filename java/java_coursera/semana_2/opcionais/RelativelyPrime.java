/* 
Enunciado:
Write a program RelativelyPrime that takes an integer command-line argument n and prints an n-by-n 
table such that there is an * in row i and column j if the gcd of i and j is 1 
(i and j are relatively prime) and a space in that position otherwise.
*/

package opcionais;
public class RelativelyPrime {
    public static void main(String[] args)
    {
        int num = Integer.parseInt(args[0]);
        for (int i = 0; i <= num; i++)
        {
            for (int j = 0; j <= num; j++) {
                if (i==0 && j==0) {
                    System.out.print("  ");
                } else if (i==0 && j > 0) {
                    System.out.print(String.format("%2d", j));
                } else if (j==0 && i > 0) {
                    System.out.print(String.format("%2d", i));
                } else {
                    if (gcdEuclides(i, j) == 1) {
                        System.out.print(String.format("%2s", "*"));
                    } else {
                        System.out.print(String.format("%2s", ""));
                    }
                }
                System.out.print(" ");
            }
            System.out.print("\n");
        }
    }

    public static int gcdEuclides(int num1, int num2)
    {
        int a = Math.max(num1, num2);
        int b = Math.min(num1, num2);
        int resto;
        if (b == 0) return a;
        while (b != 0) {
            resto = a%b;
            a = b;
            b = resto;
        }
        return a;
    }
}
