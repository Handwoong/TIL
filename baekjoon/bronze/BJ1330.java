/*
 문제 : 두 수 비교하기
*/

import java.util.*;

public class BJ1330 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int a, b;
		a = scan.nextInt();
		b = scan.nextInt();
		
		if (a>b) {
			System.out.print(">");
		} else if (a<b) {
			System.out.print("<");
		} else {
			System.out.print("==");
		}
	}
}
