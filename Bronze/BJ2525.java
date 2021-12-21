/*
 문제 : 오븐 시계
*/

import java.util.*;

public class BJ2525 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int h, m, a, ma = 0;
        h = scan.nextInt();
        m = scan.nextInt();
        a = scan.nextInt();

        ma = m+a;
        if(ma >= 60) {
            ma %= 60;
            h += (m+a)/60;
            h %= 24;
        }
        System.out.println(h+" "+ma);
    }
}
