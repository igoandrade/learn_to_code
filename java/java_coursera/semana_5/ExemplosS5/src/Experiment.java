public class Experiment {
    public static int binomial(int N) 
    {
        int heads = 0;
        for (int j = 0; j < N; j++)
        {
            if (StdRandom.bernoulli(0.5))
            {
                heads++;
            }
        }
        return heads;   
    }
    public static void main(String[] args) {
        int N = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]);

        int [] freq = new int [N+1];
        for (int t = 0; t < trials; t++)
            freq[binomial(N)]++;
        
        double [] normalized = new double[N+1];
        for (int i = 0; i <= N; i++)
            normalized[i] = (double) freq[i] / trials;
        StdStats.plotBars(normalized);

        double mean = N / 2.0;
        double stddev = Math.sqrt(N) / 2.0;
        double [] phi = new double[N+1];
        for (int i = 0; i <= N; i++)
            phi[i] = Gaussian.pdf(i, mean, stddev);
        StdStats.plotLines(phi);
    }
}
