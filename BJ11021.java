/*
 문제 : A+B - 7
*/

import java.util.*;

public class BJ11021 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int t, a, b;
		t = scan.nextInt();
		
		for(int i = 1; i <= t; i++) {
			a = scan.nextInt();
			b = scan.nextInt();
			System.out.println("Case #"+i+":"+" "+(a+b));
		}
	}
}
