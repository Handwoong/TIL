/*
 ¹®Á¦ : °ö¼À
*/

import java.util.*;

public class BJ2588 {
	public static void main(String args[]) {
		Scanner scan = new Scanner(System.in);
		int a, b, c, d;
		a = scan.nextInt(); // 472
		b = scan.nextInt(); // 385
		/*
		c = (b-((b/100)*100))/10; // 10ÀÇ ÀÚ¸®
		d = (b-((b/100)*100))-((b-((b/100)*100))/10*10); // 1ÀÇ ÀÚ¸®
		System.out.println(a*d);
		System.out.println(a*c);
		System.out.println(a*(b/100));
		System.out.println(a*b);
		*/
		c = b%100; // 85
		d = b%10;  // 5
		System.out.println(a*d);
		System.out.println(a*(c/10));
		System.out.println(a*(b/100));
		System.out.println(a*b);
	}
}
