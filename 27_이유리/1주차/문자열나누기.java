class Solution {
    public int solution(String s) {
        int answer = 0;		// 분해한 문자열의 개수
        int count = 0;
        char first = '0';	// 첫 글자. 초기값은 '0'으로 설정
        
        for(int i = 0; i < s.length(); i++) {
        	if(first == '0') {			// '0'이면 아직 첫 글자가 선택되지 않음
        		first = s.charAt(i);	// 첫 글자를 first에 넣는다.
        	}
        	if(s.charAt(i) == first)	// 현재 글자가 first값과 같다면
        		count++;				// count++
        	else
        		count--;				// first와 다르다면 count--
        	
        	if(count == 0) {			// count가 0이 되면
        		answer++;				// answer++하여 문자열이 분리되었음을 표시
        		first = '0';			// first 초기화
        	}
        }
        if(count > 0)
        	answer++;
        
        return answer;
    }
}
