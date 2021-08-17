public class DiscreteDistribution 
{
    public static void main(String[] args) 
    {
        int m = Integer.parseInt(args[0]);
        int n = args.length - 1;
        int[] s = new int[n+1];
        int sMax;
        for (int i = 1; i < n+1; i++)
        {
            for (int j = 1; j <= i; j++)
            {
                s[i] += Integer.parseInt(args[j]);
            }
        }
        sMax = s[s.length - 1];
        for (int i = 0; i < m; i++)
        {
            int r = (int) (Math.random() * sMax);
            for (int j = 1; j <= n; j++)
            {
                if (s[j-1] <= r && r < s[j])
                {
                    System.out.print(j + " ");
                }
            }
        }   
    }
}
