public class TrinomialDP 
{

    // Returns the trinomial coefficient T(n, k).
    public static long trinomial(int n, int k)
    {
        if (k < -n || k > n) return 0;
        int N = Math.max(n, 10);
        long[][] T = new long[N+1][2*N + 1];
        T[0][N] = 1;
        T[1][N-1] = 1;
        T[1][N] = 1;
        T[1][N+1] = 1;
        T[N][0] = 1;
        T[N][2*N] = 1;
        for (int i = 2; i <= N; i++){
            for (int j = 1; j < 2*N; j++){
                T[i][j] = T[i-1][j-1] + T[i-1][j] + T[i-1][j+1];
            }
        }
        return T[n][Math.abs(k-N)];

    }

    // Takes two integer command-line arguments n and k and prints T(n, k).
    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        int k = Integer.parseInt(args[1]);
        StdOut.println(trinomial(n, k));       
    }
}
