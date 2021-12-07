/*
 문제 : 윤년
*/

import java.util.*;

public class BJ2753 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int a;
		a = scan.nextInt();
		
		if (a%4 == 0 && (a%100 != 0 || a%400 == 0)) {
			System.out.print("1");
		} else {
			System.out.print("0");
		}
	}
}
