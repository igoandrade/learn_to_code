package opcionais;

/*
Enunciado:
    Write a program Kary that takes two integer command line arguments i and k and converts i to base k. 
    Assume that i is an integer in Java’s long data type and that k is an integer between 2 and 16. 
    For bases greater than 10, use the letters A through F to represent the 11th through 16th digits, 
    respectively. 
*/

public class Kary {
    public static void main(String[] args) {
        long i = Long.parseLong(args[0]);
        int k = Integer.parseInt(args[1]);
        
        
        System.out.println(i);
        System.out.println(k);

    }
}
