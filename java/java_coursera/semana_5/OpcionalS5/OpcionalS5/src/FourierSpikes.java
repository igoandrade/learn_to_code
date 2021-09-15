public class FourierSpikes {
    public static double fourier(int n, double t) {
        double sum = 0;
        for (int i = 1; i <= n; i++)
        {
            sum += Math.cos(i * t);
        }
        return (double) (sum / n); 
    }
    public static void main(String[] args) {
        int p = 500;
        int n = Integer.parseInt(args[0]);
        double [] t = new double[p+1];
        double [] f = new double[p+1];
        for (int i = 0; i <= p; i++)
        {
            t[i] = -10.0 + i * 20/p;
            f[i] = fourier(n, t[i]);
        }

        StdDraw.setXscale(-10.0, +10.0);
        StdDraw.setYscale(-1.5, 1.5);
        StdDraw.setPenRadius(0.002);
        StdDraw.line(-10.0, 1.0, 10.0, 1.0);
        StdDraw.line(-10.0, -1.0, 10.0, -1.0);
        for (int i = 0; i < p; i++)
            StdDraw.line(t[i], f[i], t[i+1], f[i+1]);
        

    }
}
