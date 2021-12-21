/*
 문제 : 주사위 세개
*/

import java.util.*;

public class BJ2480 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int a, b, c, result = 0;
        a = scan.nextInt();
        b = scan.nextInt();
        c = scan.nextInt();

        if(a == b && b == c) {
            result = 10000+a*1000;
        } else if(a == b || b == c || a == c) {
            if(a == b || a == c) {
                result = 1000+a*100;
            } else {
                result = 1000+b*100;
            }
        } else {
            if(a > b && a > c) {
                result = a*100;
            } else if(b > a && b > c) {
                result = b*100;
            } else {
                result = c*100;
            }
        }
        System.out.println(result);
    }
}
