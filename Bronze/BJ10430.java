/*
 문제 : 나머지
*/

import java.util.Scanner;
public class BJ10430 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int A, B, C;
		A = scan.nextInt();
		B = scan.nextInt();
		C = scan.nextInt();
		System.out.println((A+B)%C);
		System.out.println(((A%C) + (B%C))%C);
		System.out.println((A*B)%C);
		System.out.println(((A%C)*(B%C))%C);
	}
}