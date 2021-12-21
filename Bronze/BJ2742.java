/*
 문제 : 기찍 N
*/

import java.util.*;

public class BJ2742 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int a;
		a = scan.nextInt();
		int result = a;
		
		for(int i = 0; i < a; i++) {
			System.out.println(result);
			result = result - 1;
		}
	}
}
