/*
 문제 : A+B - 3
*/

import java.util.*;

public class BJ10950 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int a, b, t;
		t = scan.nextInt();
		
		for(int i = 0; i < t; i++) {
			a = scan.nextInt();
			b = scan.nextInt();
			System.out.println(a+b);
		}
	}
}
