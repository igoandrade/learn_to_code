/*
Enunciado:
    Ramanujan’s taxi. Srinivasa Ramanujan was an Indian mathematician who became famous for 
    his intuition for numbers. When the English mathematician G. H. Hardy came to visit him 
    one day, Hardy remarked that the number of his taxi was 1729, a rather dull number. 
    To which Ramanujan replied, “No, Hardy! No, Hardy! It is a very interesting number. 
    It is the smallest number expressible as the sum of two cubes in two different ways.” 
    Verify this claim by writing a program that takes an integer command-line argument n 
    and prints all integers less than or equal to n that can be expressed as the sum of 
    two cubes in two different ways. In other words, find distinct positive integers 
    a, b, c, and d such that a^3 + b^3 = c^3 + d^3. Use four nested for loops.
*/

package opcionais;

public class RamanujansTaxi
{
    public static void main(String[] args)
    {
        int num = Integer.parseInt(args[0]);
        System.out.println("Número de Ramanujan: pode ser expresso como soma de cubos de duas maneiras diferentes.");


        if (isRamanujansNumber(num)) 
        {
            System.out.println("O número " + num + " é um número de Ramanujan.");
        } else 
        {
            System.out.println("O número " + num + " não é um número de Ramanujan.");
        }
        
    }

    public static boolean isRamanujansNumber(int num)
    {
        int qtd_RN = 0;
        for (int i = 1; i <= (num-1)/(i*i); i++) 
        {
            for (int j = i; j <= (num-1)/(j*j); j++) {
                boolean teste = Math.pow(i,3) + Math.pow(j,3) == num;
                if (teste) 
                {
                    qtd_RN += 1;
                    System.out.println("(" + i + "," + j + ")");
                }
            }
        }
        if (qtd_RN == 2) return true; else return false;    }
}