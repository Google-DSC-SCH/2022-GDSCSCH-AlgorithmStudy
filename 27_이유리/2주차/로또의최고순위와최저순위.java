class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {};
        int count = 0;	// 당첨이 확실한 번호의 수
        int zero = 0;	// 지워진 번호의 수
        
        for(int i = 0; i < 6; i++) {
        	if(lottos[i] == 0) {
        		zero++;
        		continue;
        	}
        	for(int j = 0; j < 6; j++) {
        		if(lottos[i] == win_nums[j])
        			count++;
        	}
        }
        
        if(count == 0) {
        	if(zero == 0)
        		answer = new int[] {6, 6};
        	else
        		answer = new int[]{ 7 - zero, 6};
        }
        else {
        	answer = new int[]{ 7 - (count + zero), 7 - count};
        }
        
        return answer;
    }
}
