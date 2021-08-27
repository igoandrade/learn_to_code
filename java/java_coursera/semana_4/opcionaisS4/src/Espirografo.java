public class Espirografo
{
    public static void main(String[] args)
    {
        double R = Double.parseDouble(args[0]);
        double r = Double.parseDouble(args[1]);
        double a = Double.parseDouble(args[2]);
        int n = 10000;
        double lim = R + 2 * r + a;
        StdDraw.setScale(-lim, +lim);
        StdDraw.setPenRadius(0.0001);
        for (int i = 0; i < n; i++)
        {   
            double t = 28 * Math.PI * i/n;
            double x = (R + r) * Math.cos(t) - (r + a) * Math.cos((R + r) * t / r);
            double y = (R + r) * Math.sin(t) - (r + a) * Math.sin((R + r) * t / r);
            StdDraw.point(x, y);
        }
    }
}