public class Inversions {

    // Return the number of inversions in the permutation a[].
    public static long count(int[] a)
    {
        int n = a.length;
        int soma = 0;
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (a[i] > a[j]) soma++;
            }
        }
        return soma;
    }

    // Return a permutation of length n with exactly k inversions.
    public static int[] generate(int n, long k)
    {
        int[] a = new int[n];
        for (int i = 0; i < n; i++)
        {
            a[i] = i;
        }
        int j = n - 1;
        while (k > 0)
        {
            int m = (int) Math.min(k, j);
            for (int i = 0; i < m; i++)
            {
                int aux = a[n - 1 - i];
                a[n - 1 - i] = a[n - 1 - i - 1];
                a[n - 1 - i - 1] = aux;
            }
            k = k - m;
            j = j - 1;
        }

        return a;
    }

    // Takes an integer n and a long k as command-line arguments,
    // and prints a permutation of length n with exactly k inversions.
    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        long k = Long.parseLong(args[1]);
        int[] a = generate(n, k);
        StdOut.print(a[0]);
        for (int i = 1; i < n; i++)
            StdOut.print(" " + a[i]);
    }
}