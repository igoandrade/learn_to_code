public class ThueMorse {
    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        boolean[] tmSeq = new boolean[n];
        int nSquared = 1;
        while (nSquared < n)
        {
            nSquared *= 2;
        }
        boolean[] temp = new boolean[nSquared];
        int k = 1;
        while (k != nSquared) 
        {
            for (int i = 0; i < k; i++)
            {
                temp[k+i] = !temp[i];
            }
            k *= 2;
        }
        for (int i = 0; i < n; i++)
        {
            tmSeq[i] = temp[i];
        }


        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (tmSeq[i] == tmSeq[j])
                {
                    System.out.print("+  ");
                } else
                {
                    System.out.print("-  ");
                }
                
                
            }
            System.out.println();
        }
    }
}
