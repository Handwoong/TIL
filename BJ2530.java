/*
 문제 : 인공지능 시계
*/

import java.util.*;

public class BJ2530 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int h, m, s, a, sa = 0;
        h = scan.nextInt();
        m = scan.nextInt();
        s = scan.nextInt();
        a = scan.nextInt();

        sa = s+a;
        if(sa >= 60) {
            sa %= 60;
            m += (s+a)/60;
            h += m/60;
            h %= 24;
            m %= 60;
        }
        System.out.println(h+" "+m+" "+sa);
    }
}
