public class RevesPuzzle
{
    private static void hanoi(int n, int k, String from, String aux, String to) {
        if (n == 0) {
             StdOut.println();
             return;
        }
        hanoi(n - 1, k, from, to, aux);
        StdOut.print("Move disc " + (n + k) + " from " + from + " to " + to);
        hanoi(n - 1, k, aux, from, to);
    }
    private static void rev(int n, String from, String aux, String to, String aux2) {
        int k = (int) (n + 1 - Math.round(Math.sqrt(2 * n + 1)));
        if (k == 0){
            StdOut.print("Move disc " + 1  + " from " + from + " to " + to);
            return;
        }
        rev(k, from , to, aux , aux2);
        hanoi(n-k,k, from, aux2, to);
        rev(k,aux,from,to,aux2);
    }

    public static void main(String[] args)
    {
        int n = Integer.parseInt(args[0]);
        rev(n, "A", "B", "D", "C");
    }
}