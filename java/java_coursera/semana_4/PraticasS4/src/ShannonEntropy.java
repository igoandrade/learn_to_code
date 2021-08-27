public class ShannonEntropy
{
    public static void main(String[] args)
    {
        int m = Integer.parseInt(args[0]);
        int [] p = new int[m];
        double sum = 0.0;
        int n = 0;
        while (!StdIn.isEmpty())
        {
            int x = StdIn.readInt();
            p[x-1]++;
            n++;
        }
        for (int i = 0; i < m; i++)
        {
            double x = (double) p[i] / n;
            if (p[i] != 0) sum -= x * Math.log(x) / Math.log(2.0);
        }
        StdOut.printf("%.4f%n", sum);
    }
}