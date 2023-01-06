package level1;

import java.util.*;


public class PGS_140108 {


    public static int solution(String s) {
        char first = s.charAt(0);
        int count = 0;
        int diff = 0;
        int answer = 0;
      
        for (int i = 0; i < s.length(); i++) {
            if (count == diff) {
                answer++;
                first = s.charAt(i);
            }
            if (first == s.charAt(i)) {
                count++;
            } else {
                diff++;
            }
        }
        return answer;
    }
  
}
