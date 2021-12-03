public class ActivationFunction {

    // Returns the Heaviside function of x.
    public static double heaviside(double x)
    {
        if (x < 0)
            return 0.0;
        else if (x == 0)
            return 0.5;
        else
            return 1.0;
    }

    // Returns the sigmoid function of x.
    public static double sigmoid(double x)
    {
        double s = 1 / (1 + Math.exp(-x));
        return s;
    }

    // Returns the hyperbolic tangent of x.
    public static double tanh(double x)
    {
        return Math.tanh(x);
    }

    // Returns the softsign function of x.
    public static double softsign(double x)
    {
        double s = x / (1 + Math.abs(x));
        return s;
    }

    // Returns the square nonlinearity function of x.
    public static double sqnl(double x)
    {
        if (x <= -2)
            return -1.0;
        else if (x < 0)
            return x + x * x / 4.0;
        else if (x < 2)
            return x - x * x / 4.0;
        else 
            return 1.0;
    }

    // Takes a double command-line argument x and prints each activation
    // function, evaluated, in the format (and order) given below.
    public static void main(String[] args)
    {
        double x = Double.parseDouble(args[0]);
        System.out.printf("%9s(%.1f) = ", "heaviside", x);
        System.out.println(heaviside(x));
        System.out.printf("%9s(%.1f) = ", "sigmoid", x);
        System.out.println(sigmoid(x));
        System.out.printf("%9s(%.1f) = ", "tanh", x);
        System.out.println(tanh(x));
        System.out.printf("%9s(%.1f) = ", "softsign", x);
        System.out.println(softsign(x));
        System.out.printf("%9s(%.1f) = ", "sqnl", x);
        System.out.println(sqnl(x));
    }
}