public class Checkerboard 
{
    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        double r = 0.500;
        StdDraw.setScale(0, n);

        for (int i = 0; i < n; i++)
        {
            double cx = (double) i + r;
            for (int j = 0; j < n; j++)
            {
                double cy = (double) j + r;
                
                if ((i + j) % 2 == 0) 
                {
                    StdDraw.setPenColor(StdDraw.BLUE);
                    
                } else 
                {
                    StdDraw.setPenColor(StdDraw.LIGHT_GRAY);
                }
                StdDraw.filledSquare(cx, cy, r);
            }
        }
        
        StdOut.println();
    }
}
