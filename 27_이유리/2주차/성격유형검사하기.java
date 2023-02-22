class Solution {
	
	char tmp_type;
	int plus;
	
    public String solution(String[] survey, int[] choices) {
      
    	String answer = "";
    	char[] type = {'R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'};
    	int[] type_num = new int[8];
         
        for(int i = 0; i < choices.length; i++) {
        	if(choices[i] < 4) {		// 선택지가 4이하인 경우
        		plus = 4 - choices[i];
        		tmp_type = survey[i].charAt(0);
        	}
        	else if (choices[i] > 4) {	// 선택지가 4 이상인 경우
        		plus = choices[i] - 4;
        		tmp_type = survey[i].charAt(1);
        	}
        	else						// 선택지가 4인 경우
        		continue;
        	
        	for(int j = 0; j < 8; j++) {	// 성격 유형별 점수 표시
				if(type[j] == tmp_type) {
					type_num[j] += plus;
					break;
				}
        	}
        }
        
        for(int i = 0; i < 8; i+=2) {		// 성격 유형 점수를 비교하여 어떤 유형에 더 가까운지 탐색
        	if(type_num[i] >= type_num[i + 1])
        		answer += String.valueOf(type[i]);
        	else
        		answer += String.valueOf(type[i + 1]);
        }
        
        return answer.toString();
    }
}
