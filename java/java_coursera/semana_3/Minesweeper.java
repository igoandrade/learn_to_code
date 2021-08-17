public class Minesweeper {
    public static void main(String[] args){
        int m = Integer.parseInt(args[0]);
        int n = Integer.parseInt(args[1]);
        int k = Integer.parseInt(args[2]);
        int[][] tab = new int[m][n];
        int[][] tabBase = new int[m+2][n+2];

/*
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                System.out.print(tab[i][j] + "  ");

            }
            System.out.println();
        }
*/        
        while (k>0)
        {
            int i = (int) (Math.random() * m);
            int j = (int) (Math.random() * n);
            
            if (tab[i][j] != 1){
                tab[i][j] = 1;
                //System.out.println(i + " " + j);
                k--;
            }
            
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                tabBase[i+1][j+1] = tab[i][j];
            }
            //System.out.println();
        }

/*
        for (int i = 0; i < m+2; i++)
        {
            for (int j = 0; j < n+2; j++)
            {
                System.out.print(tabBase[i][j] + "  ");
            }
            System.out.println();
        }
*/
        for (int i = 1; i < m+1; i++)
        {
            for (int j = 1; j < n+1; j++)
            {   
                int qtdMinas = 0;
                if (tabBase[i][j] == 1)
                {
                    System.out.print("*  ");
                } else
                {
                    qtdMinas = tabBase[i-1][j-1] + tabBase[i-1][j] + tabBase[i-1][j+1] + tabBase[i][j-1] + tabBase[i][j+1] + tabBase[i+1][j-1] + tabBase[i+1][j] + tabBase[i+1][j+1];
                    System.out.print(qtdMinas + "  ");
                }
                
            }
            System.out.println();
        }
    }
}
