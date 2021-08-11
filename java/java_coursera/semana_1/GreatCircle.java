/* 
Floating-point numbers and the Math library. The great-circle distance is the length 
of the shortest path between two points (x1,y1) and (x2,y2) on the surface of a sphere, 
where the path is constrained to be along the surface.

Write a program GreatCircle.java that takes four double command-line arguments 
x1, y1, x2, and y2 — the latitude and longitude (in degrees) of two points on 
the surface of the earth—and prints the great-circle distance (in kilometers) 
between them. Use the following Haversine formula

    distance = 2r * arcsin(sqrt(sin^2((x2-x1)/2) + cos x1 * cos x2 * sin^2((y2-y1)/2)))

where r=6,371.0 is the mean radius of the Earth (in kilometers).
*/ 



public class GreatCircle {
    public static void main(String[] args) {
        double x1 = Double.parseDouble(args[0]);
        double y1 = Double.parseDouble(args[1]);
        double x2 = Double.parseDouble(args[2]);
        double y2 = Double.parseDouble(args[3]);

        double r = 6371.0;

        x1 = Math.toRadians(x1);
        x2 = Math.toRadians(x2);
        y1 = Math.toRadians(y1);
        y2 = Math.toRadians(y2);

        double cosX1 = Math.cos(x1);
        double cosX2 = Math.cos(x2); 
        double squareSinDX = Math.pow(Math.sin((x2-x1)/2.0), 2);
        double squareSinDY = Math.pow(Math.sin((y2-y1)/2.0), 2);

        double rootArg = squareSinDX + cosX1 * cosX2 * squareSinDY;

        double distance = 2.0 * r * Math.asin(Math.sqrt(rootArg));

        System.out.println(distance + " kilometers");
    }
}
