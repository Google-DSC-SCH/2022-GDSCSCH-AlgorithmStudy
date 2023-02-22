class Solution {
    public String solution(int n) {
        String answer = "";
        String[] rest = {"4", "1", "2"};
        
        while(n > 0){
            int r = n % 3;
            n = n / 3;
            
            if(r == 0) n--;
            
            answer = rest[r] + answer;
        }
        
        return answer;
    }
}
