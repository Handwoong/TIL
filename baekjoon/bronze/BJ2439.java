/*
 문제 : 별 찍기 - 2
*/

import java.util.*;

public class BJ2439 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int n;
        n = scan.nextInt();

        for(int i = 1; i <= n; i++) {
            for(int j = n-i; j > 0; j--) {
                System.out.print(" ");
            }
            for(int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
}
