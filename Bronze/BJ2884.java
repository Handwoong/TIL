/*
 문제 : 알람 시계
*/

import java.util.*;

public class BJ2884 {
	public static void main(String args[]) {
	Scanner scan = new Scanner(System.in);
	int H = 0, M = 0;
	H = scan.nextInt();
	M = scan.nextInt();
	M = M-45;
	if(H == 0 && M < 0) {
		H = 23;
		M = 60+M;
		System.out.print(H+" "+M);
	} else if (H != 0 && M < 0) {
		H = H-1;
		M = 60+M;
		System.out.print(H+" "+M);
	} else {
		System.out.print(H+" "+M);
	}
}
}
