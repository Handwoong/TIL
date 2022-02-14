// 문제 : 0 = not cute / 1 = cute

import java.util.*;

public class BJ10886 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int N, vote, A = 0, B = 0;
        N = scan.nextInt();

        for(int i = 0; i < N; i++) {
            vote = scan.nextInt();
            if(vote == 1) {
                A++;
            } else {
                B++;
            }
        }
        if(A > B) {
            System.out.print("Junhee is cute!");
        } else {
            System.out.print("Junhee is not cute!");
        }
    }
}
