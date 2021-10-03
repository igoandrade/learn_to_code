public class Ramanujan {

    // Is n a Ramanujan number?
    public static boolean isRamanujan(long n)
    {
        long aMax = Math.round(Math.cbrt(n/2.0));
        int qtd = 0;
        for (long a = 1; a < aMax; a++)
        {
            
            long b = Math.round(Math.cbrt(n - a*a*a));
            if (a*a*a + b*b*b == n)
            {
                qtd  = qtd + 1;
                continue;
            } 
        }
        if (qtd == 2) return true;
        return false;

    }

    // Takes a long integer command-line arguments n and prints true if
    // n is a Ramanujan number, and false otherwise.
    public static void main(String[] args)
    {
        long n = Long.parseLong(args[0]);
        StdOut.println(isRamanujan(n));
    }
}
