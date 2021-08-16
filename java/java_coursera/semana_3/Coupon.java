public class Coupon
{
    public static void main(String[] args)
    {
        int M = Integer.parseInt(args[0]);
        int num_jogadas = Integer.parseInt(args[1]);
        int sum_cards = 0;
        for (int i = 0; i < num_jogadas; i++)
        {   
            int cards = test(M);
            sum_cards += cards;
        }
        double avg = (double) sum_cards/num_jogadas;
        double real_avg = M * Math.log(M) + 0.57751 * M;
        double error = Math.abs(real_avg - avg)/real_avg;
        System.out.println("Resultado Experimental: " + avg);
        System.out.println("Resultado Teórico: " + real_avg);
        System.out.println("Erro (%): " + error);
    }

    public static int test(int M){
        int cards = 0;
        int distinct = 0;
        boolean[] found = new boolean[M];
        while (distinct < M)
        {
            int r = (int) (Math.random() * M);
            cards++;
            if (!found[r])
            {
                distinct++;
                found[r] = true;
            }
        }
        return cards;
    }
}
