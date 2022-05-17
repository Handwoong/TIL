/*
 문제 : 과자
*/

import java.util.*;

public class BJ10156 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int K, N, M, result = 0;
        K = scan.nextInt();
        N = scan.nextInt();
        M = scan.nextInt();
        result = K*N-M;
        if(result < 0) {
            result = 0;
        }
        System.out.println(result);
    }
}
