/*
 문제 : R2
*/

import java.util.*;

public class BJ3046 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int R1, R2, S;
        R1 = scan.nextInt();
        S = scan.nextInt();
        R2 = 2*S-R1;
        System.out.print(R2);
    }
}
