public class Divisors {

    // Returns the greatest common divisor of a and b.
    public static int gcd(int a, int b)
    {
        if (a == 0 && b == 0)
            return 0;
        a = Math.abs(a);
        b = Math.abs(b);
        int maior = Math.max(a, b);
        int menor = Math.min(a, b);
        while (menor != 0)
        {
            int tmp = maior % menor;
            maior = menor;
            menor = tmp;
        }
        return maior;
    }

    // Returns the least common multiple of a and b.
    public static int lcm(int a, int b)
    {
        if (a == 0 && b == 0)
            return 0;
        return Math.abs(a * b) / gcd(a, b);
    }

    // Returns true if a and b are relatively prime; false otherwise.
    public static boolean areRelativelyPrime(int a, int b)
    {
        if (gcd(a, b) == 1)
            return true;
        else
            return false;
    }

    // Returns the number of integers between 1 and n that are
    // relatively prime with n.
    public static int totient(int n)
    {
        int phi = 0;
        for (int i = 1; i < n; i++)
        {
            if (areRelativelyPrime(i, n))
                phi++;
        }
        return phi;
    }

    // Takes two integer command-line arguments a and b and prints
    // each function, evaluated in the format (and order) given below.
    public static void main(String[] args)
    {
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        System.out.printf("gdc(%d, %d) = %d%n", a, b, gcd(a, b));
        System.out.printf("lcm(%d, %d) = %d%n", a, b, lcm(a, b));
        System.out.printf("areRelativelyPrime(%d, %d) = %b%n", a, b, areRelativelyPrime(a, b));
        System.out.printf("totient(%d) = %d%n", a, totient(a));
        System.out.printf("totient(%d) = %d%n", b, totient(b));

    }   
}