/*
1 - Strings and command-line arguments. Write a program HelloGoodbye.java that takes two names 
as command-line arguments and prints hello and goodbye messages as shown below (with the names 
for the hello message in the same order as the command-line arguments and with the names for 
the goodbye message in reverse order).
*/


public class HelloGoodbye {
    public static void main(String[] args) {
        
        String primeiroNome = args[0];
        String segundoNome = args[1];

        System.out.println("Hello " + primeiroNome + " and " + segundoNome + ".");
        System.out.println("Goodbye " + segundoNome + " and " + primeiroNome + ".");
    } 
}
