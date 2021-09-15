public class LargestInteger {
    public static int lg(int n)
    {
        int l = 0;
        while (n > 1)
        {
            n = n / 2;
            l++;
        }
        return l;
    }
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        StdOut.println(lg(n));
    }
}
