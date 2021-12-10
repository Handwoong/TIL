// 문제 : 학점계산
import java.util.*;

public class BJ2754 {
    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        String A = "";
        double score = 0;
        A = scan.next();
        String first = A.substring(0, 1);
        String second = A.substring(1);

        if(first.equals("A")) {
            score += 4.0;
        } else if(first.equals("B")) {
            score += 3.0;
        } else if(first.equals("C")) {
            score += 2.0;
        } else if(first.equals("D")) {
            score += 1.0;
        }

        if(second.equals("+")) {
            score += 0.3;
        } else if(second.equals("-")) {
            score -= 0.3;
        }
        System.out.print(score);
    }
}

