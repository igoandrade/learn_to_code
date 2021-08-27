public class WorldMap 
{
    public static void main(String[] args)
    {
        int width = StdIn.readInt();
        int height = StdIn.readInt();
        
        StdDraw.setCanvasSize(width, height);
        StdDraw.setXscale(0, width);
        StdDraw.setYscale(0, height);
        while(!StdIn.isEmpty())
        {
            String state = StdIn.readString();
            StdOut.println(state);
            int v = StdIn.readInt();
            double[] x = new double[v];
            double[] y = new double[v];
            for (int i = 0; i < v; i++)
            {
                x[i] = StdIn.readDouble();
                y[i] = StdIn.readDouble();
            }
            StdDraw.polygon(x, y);
        }

    }
}
