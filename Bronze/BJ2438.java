/*
 문제 : 별 찍기 - 1
*/

import java.util.*;

public class BJ2438 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int n;
        n = scan.nextInt();

        for(int i = 0; i < n; i++) {
            for(int j = 0; j <= i; j++) {
                System.out.print("*");
            }
            System.out.print("\n");
        }
    }
}
