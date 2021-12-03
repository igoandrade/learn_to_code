public class PlayThatTune {
    public static double[] tone(double hz, double duration)
    {
        int N = (int) (44100 * duration);
        double[] a = new double[N+1];
        for (int i = 0; i <= N; i++)
        {
            a[i] = Math.sin(2 * Math.PI * i * hz / 44100);
        }
        return a;
    }
    public static void main(String[] args)
    {
        double tempo = Double.parseDouble(args[0]);
        while (!StdIn.isEmpty())
        {
            int pitch = StdIn.readInt();
            double duration = StdIn.readDouble() * tempo;
            double hz = 440 * Math.pow(2, pitch/12.0);
            double[] a = PlayThatNote.tone(hz, duration);
            StdAudio.play(a);
        }
        StdAudio.close();
    }
}
