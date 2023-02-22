class Solution {
    public String solution(String new_id) {
        String answer = "";
        char c;
        
        answer = new_id;
        
        // 1단계
        answer = answer.toLowerCase();
        
        // 2단계
        answer = answer.replaceAll("[^a-z0-9-_.]", "");	// 정규식을 사용하여 소문자 숫자 - _ .을 제외한 모든 문자들을 제거한다.
        
        // 3단계
        answer = answer.replaceAll("[.]{2,}", ".");	// 정규식을 사용하여 마침표가 2번 이상 반복되는 경우 마침표 하나로 대체한다.
        
        // 4단계
        answer = answer.replaceAll("^[.]|[.]$", "");	// 정규식을 사용하여 첫 문자 혹은 끝 문자가 마침표인 경우 제거한다.
        
        // 5단계
        if(answer.equals(""))
        	answer = "a";
        
        // 6단계
        if(answer.length() > 15) {
        	answer = answer.substring(0, 15);
        	answer = answer.replaceAll("[.]$", "");
        }
        
        // 7단계
        if(answer.length() < 3) {
        	c = answer.charAt(answer.length() - 1);
        	while(answer.length() < 3) {
        		answer += c;
        	}
        }
        return answer;
    }
}
