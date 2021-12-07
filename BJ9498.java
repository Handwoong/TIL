/*
 문제 : 시험 성적
*/

import java.util.*;

public class BJ9498 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int a;
		a = scan.nextInt();
		
		if (a >= 90) {
			System.out.println("A");
		} else if (a < 90 && a >= 80) {
			System.out.println("B");
		} else if (a < 80 && a >= 70) {
			System.out.println("C");
		} else if (a < 70 && a >= 60) {
			System.out.println("D");
		} else {
			System.out.println("F");
		}
	}
}
