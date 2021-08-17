public class Birthday {
    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        int trials = Integer.parseInt(args[1]); 
        int[] countPeople = new int[n+1];
        double[] prop = new double[n+1];
        for (int t = 0; t < trials; t++)
        {
            int b; 
            int[] ani = new int[n+1];
            boolean test = false;
            int p = 0;
            while (!test) 
            {
                b = (int) (Math.random() * n);
                ani[p] = b;
                for (int i = 0; i < p; i++)
                {
                    if (b == ani[i]) {
                        test = true;
                        break;
                    }
                }
                p++;
            }
            for (int i = 0; i < n; i++) 
            {
                if (p == i+1) 
                {
                    countPeople[i]++;
                }
            }
        }
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j <= i; j++)
            {
                prop[i] += countPeople[j];
            }
            prop[i] = prop[i]/trials;
        }
        for (int k = 1; k <= n; k++)
        {
            System.out.println(k+"\t"+countPeople[k-1]+"\t"+prop[k-1]);
            if (prop[k-1] > 0.5) 
            {
                break;
            }
        }

    }
}
