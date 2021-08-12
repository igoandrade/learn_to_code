/*
Enunciado:
    Random walk. A Java programmer begins walking aimlessly. At each time step, she takes one 
    step in a random direction (either north, east, south, or west), each with probability 25%. 
    She stops once she is at Manhattan distance r from the starting point. How many steps will
    the random walker take? This process is known as a two-dimensional random walk.

    Write a program RandomWalker.java that takes an integer command-line argument r and simulates 
    the motion of a random walk until the random walker is at Manhattan distance r from the 
    starting point. Print the coordinates at each step of the walk 
    (including the starting and ending points), treating the starting point as (0, 0). 
    Also, print the total number of steps taken.
*/



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


