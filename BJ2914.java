/*
 문제 : 저작권
*/

import java.util.*;

public class BJ2914 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System. in);
        int A, I;
        A = scan.nextInt();
        I = scan.nextInt();

        System.out.print((I-1)*A+1);
    }
}
