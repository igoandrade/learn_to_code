public class MaximumSquareSubmatrix2 {

    // Returns the size of the largest contiguous square submatrix
    // of a[][] containing only 1s.
    public static int size(int[][] a)
    {
        int n = a.length;
        int m = a[0].length;
        int p = Math.min(m, n);
        int msq = 0;
        for (int len = 2; len <= p; len++)
        {
            for (int i = 0; i <= n - len; i++)
            {
                for (int j = 0; j <= m - len; j++)
                {
                    if (a[i][j] == 0)
                    {
                        continue;
                    } else
                    {
                        int soma = 0;
                        for (int lin = i; lin < i + len; lin++)
                        {
                            for (int col = j; col < j + len; col++)
                            {
                                soma = soma + a[lin][col];
                            }
                        }
                        if (soma == len * len && soma > msq)
                        {
                            msq = len;
                        }
                    }

                }

            } 
 
        }
        

        return msq;
    }

    // Reads an n-by-n matrix of 0s and 1s from standard input
    // and prints the size of the largest contiguous square submatrix
    // containing only 1s.
    public static void main(String[] args)
    {
        int n = StdIn.readInt();
        int[][] matriz = new int[n][n];
        while (!StdIn.isEmpty())
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    matriz[i][j] = StdIn.readInt();
                }
            }

        }

        int msq = size(matriz);
        StdOut.println(msq);
    }
}