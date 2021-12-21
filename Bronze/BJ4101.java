// 문제 : 크냐?

import java.util.*;

public class BJ4101 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int A, B;

        while(true) {
            A = scan.nextInt();
            B = scan.nextInt();

            if(A > B) {
                System.out.println("Yes");
            } else if(A <= B && A != 0) {
                System.out.println("No");
            } else {
                break;
            }
        }
    }
}
