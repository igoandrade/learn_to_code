/*
Enunciado:
    Write a program RandomWalkers.java that takes two integer command-line arguments r and trials. 
    In each of trials independent experiments, simulate a random walk until the random walker 
    is at Manhattan distance r from the starting point. Print the average number of steps.

    As r increases, we expect the random walker to take more and more steps. But how many more steps? 
    Use RandomWalkers.java to formulate a hypothesis as to how the average number of steps grows 
    as a function of r
*/

public class RandomWalkers
{
    public static void main(String[] args)
    {
        int r = Integer.parseInt(args[0]);
        int trails = Integer.parseInt(args[1]);
        int steps = 0;
        for (int i = 0; i < trails; i++)
        {
            int x = 0;
            int y = 0;

            int rdo = 0;
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
                
                steps += 1;
            }

        }
        double avg = (double) steps / trails;
        System.out.println("avarage number of steps = " + avg);

    }
}
