/*
Enunciado: 
    Counting primes. Write a program PrimeCounter that takes an integer command-line argument n 
    and finds the number of primes less than or equal to n. Use it to print out the number of 
    primes less than or equal to 10 million. Note : If you are not careful, your program 
    may not finish in a reasonable amount of time!
*/

package opcionais;

public class PrimeCounter 
{
    public static void main(String[] args) 
    {
        int num = Integer.parseInt(args[0]);
        int qtd = 0;
        for (int i=2; i < num; i++) {
            if (EhPrimo(i)) {
                qtd += 1;
                System.out.println(i);
            }
        }
        System.out.println("Existem " + qtd + " primos menores que " + num + ".");
    }

    public static boolean EhPrimo(int num) 
    {
        for (int i = 2; i <= num/i; i++) {
            if (num%i == 0) return false;
        }
        return true;
    }
    
}
