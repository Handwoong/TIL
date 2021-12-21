// 문제 : 세 수

import java.util.*;

public class BJ10817 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int[] arr = new int[3];

        for(int i  = 0; i <= 2; i++) {
            arr[i] = scan.nextInt();
        }
        Arrays.sort(arr);
        System.out.print(arr[1]);
    }
}
