public class AudioCollage {

    // Returns a new array that rescales a[] by a multiplicative factor of alpha.
    public static double[] amplify(double[] a, double alpha)
    {
        double[] newArr = new double[a.length];
        for (int i = 0; i < a.length; i++)
        {
            newArr[i] = alpha * a[i];
        }
        return newArr;
    }

    // Returns a new array that is the reverse of a[].
    public static double[] reverse(double[] a)
    {
        double[] newArr = new double[a.length];
        for (int i = 0; i < a.length; i++)
        {
            newArr[i] = a[a.length - i - 1];
        }
        return newArr;
    }
    // Returns a new array that is the concatenation of a[] and b[].
    public static double[] merge(double[] a, double[] b)
    {
        double[] newArr = new double[a.length + b.length];
        for (int i = 0; i < a.length; i++)
        {
            newArr[i] = a[i];
        }
        for (int i = a.length; i < a.length + b.length; i++)
        {
            newArr[i] = b[i-a.length];
        }
        return newArr;
    }

    // Returns a new array that is the sum of a[] and b[],
    // padding the shorter arrays with trailing 0s if necessary.
    public static double[] mix(double[] a, double[] b)
    {
        int n = Math.max(a.length, b.length);
        double[] newArr = new double[n];
        for (int i = 0; i < n; i++)
        {
            if (i < a.length)
                newArr[i] = newArr[i] + a[i];
            if (i < b.length)
                newArr[i] = newArr[i] + b[i];
        }
        return newArr;
    }

    // Returns a new array that changes the speed by the given factor.
    public static double[] changeSpeed(double[] a, double alpha)
    {
        int n = a.length;
        int newN = (int) (n/alpha);
        double [] newArr = new double[newN];
        for (int i = 0; i < newN; i++)
        {
            newArr[i] = a[(int) (i*alpha)];
        }
        return newArr;

    }

    // Creates an audio collage and plays it on standard audio.
    // See below for the requirements.
    public static void main(String[] args)
    {
        double [] a = StdAudio.read("singer.wav");
        double [] b = StdAudio.read("piano.wav");
        double [] c = StdAudio.read("scratch.wav");
        double [] result = merge(reverse(c), mix(changeSpeed(merge(b,b), 0.6), amplify(a, 1.5)));
        StdAudio.play(result);
    }
}