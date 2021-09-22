public class Koch {
    public static void draw(int n, double x0, double y0, double x1, double y1)
    {
        double dx = x1 - x0, dy = y1 - y0;
        double l = Math.sqrt(dx*dx + dy*dy);
        if (l <= Math.pow(1/3, n)) 
        {   StdDraw.line(x0, y0, x1, y1); return;}

        double xm = x0 + dx / 2, ym = y0 + dy / 2; 
        
        double xa = x0 + dx / 3, ya = y0 + dy / 3;
        double xb = xm - (Math.sqrt(3) / 6) * dy ; 
        double yb = ym + (Math.sqrt(3) / 6) * dx ;
        double xc = x0 + 2 * dx / 3, yc = y0 + 2 * dy / 3;

        draw(n-1, x0, y0, xa, ya);
        draw(n-1, xa, ya, xb, yb);
        draw(n-1, xb, yb, xc, yc);
        draw(n-1, xc, yc, x1, y1);
    }
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        //draw(n, 0, 0.5, 1, 0.5);
        draw(n, 0.2, 0.3, 0.5, Math.sqrt(3)*3/10+0.3);
        draw(n, 0.5, Math.sqrt(3)*3/10+0.3, 0.8, 0.3);
        draw(n, 0.8, 0.3, 0.2, 0.3);
    }
}
