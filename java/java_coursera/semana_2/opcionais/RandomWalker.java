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

public class RandomWalker
{
    public static void main(String[] args)
    {
        int r = Integer.parseInt(args[0]);

        int x = 0;
        int y = 0;
        System.out.println("("+ x + ", " + y + ")");


        int rdo = 0;
        int steps = 0;
        while (rdo != r)
        {
            double z = Math.random();
            if (z <= 0.25)
            {
                x += 1;
            } else if (z <= 0.5)
            {
                x -= 1;
            } else if (z < 0.75)
            {
                y += 1;
            } else 
            {
                y -= 1;
            }
            rdo = Math.abs(x) + Math.abs(y);
            System.out.println("("+ x + ", " + y + ")");
            
            steps += 1;
        }
        System.out.println("steps = " + steps);


    }  
}