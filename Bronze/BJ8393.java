/*
 문제 : 합
*/

import java.util.*;

public class BJ8393 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n, result = 0;
		n = scan.nextInt();
		
		for(int i = 1; i <= n; i++ ) {
			result = i+i;
			System.out.print(result);
		}
		System.out.print(result);
	}
}
