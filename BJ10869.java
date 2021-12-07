/*
 문제 : 사칙연산
*/

import java.util.Scanner;
public class BJ10869 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int a, b;
		a = scan.nextInt();
		b = scan.nextInt();
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println(a*b);
		System.out.println(a/b);
		System.out.println(a%b);
	}
}