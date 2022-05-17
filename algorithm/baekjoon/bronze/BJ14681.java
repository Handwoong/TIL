/*
 문제 : 사분면 고르기
*/

import java.util.*;

public class BJ14681 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int x, y;
		x = scan.nextInt();
		y = scan.nextInt();
		
		if (x > 0 && y > 0) {
			System.out.println("1");
		} else if (x > 0 && y < 0) {
			System.out.println("4");
		} else if (x < 0 && y > 0) {
			System.out.println("2");
		} else if (x < 0 && y < 0) {
			System.out.println("3");
		}
	}
}
