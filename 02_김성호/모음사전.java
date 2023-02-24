class Solution {
 public int solution(String word) {
        int answer = 0;
        int total= 3905;
        String aeiou="AEIOU";
        
        for(String str: word.split("")){
            //781, 156, 31, 6, 1
            total/= 5;
            answer+= total * aeiou.indexOf(str) + 1;
        }
        
        return answer;
    }
}
