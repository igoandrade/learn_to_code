/* 
2. Integers and booleans. Write a program RightTriangle that takes three int command-line 
arguments and determines whether they constitute the side lengths of some right triangle.
*/

public class RightTriangle {
    public static void main(String[] args) {
        
        int a = Integer.parseInt(args[0]);
        int b = Integer.parseInt(args[1]);
        int c = Integer.parseInt(args[2]);
        
        boolean isAllPositive = a > 0 && b > 0 && c > 0;

        boolean isPythagorean  = (c*c == a*a + b*b) || (b*b == a*a + c*c) || (a*a == b*b + c*c);

        boolean isRightTriangle = isAllPositive && isPythagorean;

        System.out.println(isRightTriangle);
    }
    
}
