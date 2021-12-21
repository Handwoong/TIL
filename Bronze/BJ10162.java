/*
 문제 : 전자레인지
*/

import java.util.*;

public class BJ10162 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int A=0, B=0, C=0, T;
        T = scan.nextInt();

        if(T % 10 == 0) {
            if(T>=300) {
                A = T/300;
                T -= 300*A;
            }
            if(T>=60) {
                B = T/60;
                T -= 60*B;
            }
            if(T>=10) {
                C = T/10;
                T -= 10*C;
            }
            System.out.print(A+" "+B+" "+C);
        } else {
            System.out.print(-1);
        }
    }
}