public class BouncingBall 
{
    public static void main(String[] args)
    {
        double rx = .200, ry = .300;
        double vx = .015, vy = .023;
        double radius = 0.05;
        StdDraw.setXscale(-1.2, +1.2);
        StdDraw.setYscale(-1.2, +1.2);
        while (true)
        {
            StdDraw.setPenColor(StdDraw.BLACK);
            StdDraw.filledSquare(0.0, 0.0, 1.0);
            //StdOut.println("vx: " + vx + "vy: " + vy);
            if (Math.abs(rx + vx) + radius > 1.0) {
                vx = -vx;
                StdAudio.playInBackground("bola.wav");
            }   
            if (Math.abs(ry + vy) + radius > 1.0) {
                vy = -vy;
                StdAudio.playInBackground("bola.wav");
            }
            rx += vx;
            ry += vy;
            //StdDraw.setPenColor(StdDraw.BLACK);
            //StdDraw.filledCircle(rx, ry, radius);
            StdDraw.picture(rx, ry, "ball2.png");
            StdDraw.pause(30);
        }
    }
}
