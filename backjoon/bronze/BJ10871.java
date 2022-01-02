/*
 문제 : X보다 작은 수
*/

import java.util.*;

public class BJ10871 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int N, X;
        N = scan.nextInt();
        X = scan.nextInt();
        int[] arr = new int[N];
        int[] arr2 = new int[N];

        for(int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
            if(X > arr[i]) {
                arr2[i] = arr[i];
                System.out.print(arr2[i]+" ");
            }
        }
    }
}
