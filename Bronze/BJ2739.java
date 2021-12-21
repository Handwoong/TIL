/*
 문제 : 구구단
*/

import java.util.*;

public class BJ2739 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int n;
		n = scan.nextInt();
		
		for(int i = 1; i<10; i++) {
			System.out.println(n+" * "+i+" = "+n*i);
		}
	}
}
