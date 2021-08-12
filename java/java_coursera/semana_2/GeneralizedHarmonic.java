/*
Enunciado:
    Generalized harmonic numbers. Write a program GeneralizedHarmonic.java that takes two integer 
    command-line arguments n and r and uses a for loop to compute the nth generalized harmonic 
    number of order r, which is defined by the following formula:
        H(n,r) = 1/1^r + 1/2^r + ... + 1/n^r
*/

public class GeneralizedHarmonic
{
    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        int r = Integer.parseInt(args[1]);

        double h = 1;

        for (int i = 2; i <= n; i++)
        {
            h += 1/Math.pow(i, r);
        }

        System.out.println(h);
    }
}