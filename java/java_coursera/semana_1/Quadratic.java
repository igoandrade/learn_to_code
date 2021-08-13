public class Quadratic {
    public static void main (String[] args) {
        double b = Double.parseDouble(args[0]);
        double c = Double.parseDouble(args[1]);

        double discriminante = b*b - 4.0*c;

        if (discriminante < 0) {
            System.out.println("Não existem raizes reais." );
        } else if (discriminante == 0) {
            double raiz = -b / 2.0;
            System.out.println("Apenas uma raiz real:");
            System.out.println(raiz);
        } else {
            double d = Math.sqrt(discriminante);

            double raiz1 = (-b + d) / 2.0;
            double raiz2 = (-b - d) / 2.0;
            
            System.out.println("Duas raizes reais distintas:");
            System.out.println(raiz1);
            System.out.println(raiz2);
        }
    }
}