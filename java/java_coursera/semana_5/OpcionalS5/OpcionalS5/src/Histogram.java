public class Histogram {
    public static int[] histogram(int[] a, int m) {
        int n = a.length;
        int[] h = new int[m];
        for (int i = 0; i < n; i++)
        {
            h[a[i]]++;
        }
        return h;
    }
    public static void main(String[] args) {
        int n = args.length - 1;
        int [] a = new int[n];
        int m = Integer.parseInt(args[n]);

        for (int i = 0; i < n; i++)
        {
            a[i] = Integer.parseInt(args[i]);
        }

        int [] h = histogram(a, m);
        for (int i = 0; i < h.length; i++)
            StdOut.println(h[i]);
    }
}
