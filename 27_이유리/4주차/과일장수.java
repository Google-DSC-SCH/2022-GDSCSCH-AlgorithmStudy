import java.util.Arrays;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        // 이익이 발생하지 않는 경우 0 return
        if(score.length < m)	
        	return 0;
        
        Arrays.sort(score);	// 오름차순 정렬
        
        // 최저 사과 점수를 구하여 이익을 계산하고 answer에 더함.
        for(int i = score.length-m; i >= 0; i-=m) {
        	answer += score[i] * m;
        }
        
        return answer;
    }
}
