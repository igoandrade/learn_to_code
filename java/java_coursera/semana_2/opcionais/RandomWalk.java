/*
Enunciado:
    2D random walk. A two-dimensional random walk simulates the behavior of a particle 
    moving in a grid of points. At each step, the random walker moves north, south, east, 
    or west with probability equal to 1/4, independent of previous moves. Write a 
    program RandomWalker that takes an integer command-line argument n and estimates how 
    long it will take a random walker to hit the boundary of a 2n-by-2n square centered 
    at the starting point.
*/

package opcionais;

public class RandomWalk {
    public static void main(String[] args) {
        int n = 123456789;
        int m = 0;
        while (n != 0)
        {
        m = (10 * m) + (n % 10);
        n = n / 10;
        }
        System.out.println(m);
    }
}
